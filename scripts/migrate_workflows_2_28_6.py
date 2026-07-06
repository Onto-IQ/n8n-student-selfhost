#!/usr/bin/env python3
"""Migrate workflow JSON files for n8n 2.28.6 compatibility."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path

WORKFLOWS_DIR = Path(__file__).resolve().parent.parent / "workflows"

OPERATION_MAP = {
    "equals": "equals",
    "notEqual": "notEquals",
    "notEquals": "notEquals",
    "contains": "contains",
    "notContains": "notContains",
    "startsWith": "startsWith",
    "endsWith": "endsWith",
    "regex": "regex",
    "isEmpty": "empty",
    "isNotEmpty": "notEmpty",
    "larger": "gt",
    "largerEqual": "gte",
    "smaller": "lt",
    "smallerEqual": "lte",
}


def new_id() -> str:
    return str(uuid.uuid4())


def migrate_set_node(node: dict) -> None:
    if node.get("type") != "n8n-nodes-base.set":
        return
    if node.get("typeVersion", 0) >= 3:
        return

    params = node.setdefault("parameters", {})
    values = params.pop("values", {})
    assignments: list[dict] = []

    for field_type in ("string", "number", "boolean", "array", "object"):
        for item in values.get(field_type, []):
            assignments.append(
                {
                    "id": new_id(),
                    "name": item["name"],
                    "value": item.get("value", False if field_type == "boolean" else ""),
                    "type": field_type,
                }
            )

    params["assignments"] = {"assignments": assignments}
    params.setdefault("options", {})
    node["typeVersion"] = 3.4


def migrate_if_node(node: dict) -> None:
    if node.get("type") != "n8n-nodes-base.if":
        return

    version = node.get("typeVersion", 1)
    params = node.setdefault("parameters", {})
    conditions = params.get("conditions", {})

    if version >= 2 and "conditions" in conditions and isinstance(conditions["conditions"], list):
        node["typeVersion"] = 2.3
        params.setdefault("options", {})
        return

    migrated: list[dict] = []

    for group_name, default_type in (
        ("string", "string"),
        ("number", "number"),
        ("boolean", "boolean"),
        ("dateTime", "dateTime"),
    ):
        for item in conditions.get(group_name, []):
            operation = OPERATION_MAP.get(item.get("operation", "equals"), item.get("operation", "equals"))
            migrated.append(
                {
                    "id": new_id(),
                    "leftValue": item.get("value1", ""),
                    "rightValue": item.get("value2", ""),
                    "operator": {
                        "type": default_type,
                        "operation": operation,
                    },
                }
            )

    params["conditions"] = {
        "options": {
            "caseSensitive": True,
            "leftValue": "",
            "typeValidation": "strict",
        },
        "conditions": migrated,
        "combinator": "and",
    }
    params.setdefault("options", {})
    node["typeVersion"] = 2.3


def migrate_agent_node(node: dict) -> None:
    if node.get("type") != "@n8n/n8n-nodes-langchain.agent":
        return
    if node.get("typeVersion", 0) >= 3:
        return

    params = node.setdefault("parameters", {})
    params.setdefault("promptType", "define")
    text = params.get("text", "={{ $json.chatInput }}")
    if text in ("={{ .chatInput }}", "={{.chatInput}}"):
        text = "={{ $json.chatInput }}"
    params["text"] = text
    params.setdefault("options", {})
    node["typeVersion"] = 3.1


def migrate_chat_trigger(node: dict) -> None:
    if node.get("type") != "@n8n/n8n-nodes-langchain.chatTrigger":
        return
    if node.get("typeVersion", 0) >= 1.4:
        return

    params = node.setdefault("parameters", {})
    options = params.setdefault("options", {})
    options.setdefault("responseMode", "lastNode")
    node["typeVersion"] = 1.4


def migrate_item_lists_to_split_out(node: dict) -> str | None:
    if node.get("type") != "n8n-nodes-base.itemLists":
        return None

    old_name = node.get("name", "Split Out")
    node["type"] = "n8n-nodes-base.splitOut"
    node["typeVersion"] = 1
    params = node.setdefault("parameters", {})
    params.setdefault("options", {})
    node.setdefault("id", new_id())
    return old_name


def migrate_memory_node(node: dict) -> None:
    if node.get("type") != "@n8n/n8n-nodes-langchain.memoryBufferWindow":
        return
    params = node.setdefault("parameters", {})
    params.setdefault("contextWindowLength", 5)
    if node.get("typeVersion", 0) < 1.3:
        node["typeVersion"] = 1.3


def ensure_settings(workflow: dict) -> None:
    settings = workflow.setdefault("settings", {})
    settings.setdefault("executionOrder", "v1")


def update_text_references(content: str) -> str:
    content = content.replace("2.8.3", "2.28.6")
    content = content.replace("2.8.x", "2.28.x")
    content = content.replace("n8n 2.8.x", "n8n 2.28.x")
    content = content.replace("Item Lists (Split Out)", "Split Out Node")
    content = content.replace("Item Lists โหมด Split Out", "Split Out Node")
    content = content.replace("Item Lists", "Split Out Node")
    return content


def migrate_workflow(workflow: dict) -> dict[str, list[str]]:
    changes: dict[str, list[str]] = {"nodes": [], "renames": []}
    renamed_nodes: dict[str, str] = {}

    for node in workflow.get("nodes", []):
        old_name = migrate_item_lists_to_split_out(node)
        if old_name:
            new_name = node.get("name", "Split Out")
            if old_name != new_name:
                renamed_nodes[old_name] = new_name
                changes["renames"].append(f"{old_name} -> {new_name}")

        before_type = node.get("type")
        before_version = node.get("typeVersion")

        migrate_set_node(node)
        migrate_if_node(node)
        migrate_agent_node(node)
        migrate_chat_trigger(node)
        migrate_memory_node(node)

        if "parameters" in node and "content" in node["parameters"]:
            node["parameters"]["content"] = update_text_references(node["parameters"]["content"])

        after_version = node.get("typeVersion")
        if before_version != after_version or before_type != node.get("type"):
            changes["nodes"].append(
                f"{node.get('name', '?')}: {before_type} v{before_version} -> "
                f"{node.get('type')} v{after_version}"
            )

    if renamed_nodes:
        connections = workflow.get("connections", {})
        for old_name, new_name in renamed_nodes.items():
            if old_name in connections:
                connections[new_name] = connections.pop(old_name)
            for conn in connections.values():
                for outputs in conn.values():
                    for routes in outputs:
                        for link in routes:
                            if link.get("node") == old_name:
                                link["node"] = new_name

    ensure_settings(workflow)
    return changes


def migrate_readme(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = update_text_references(text)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    json_files = sorted(WORKFLOWS_DIR.rglob("*.json"))
    readme_files = sorted(WORKFLOWS_DIR.rglob("README.md"))

    for readme in readme_files:
        if migrate_readme(readme):
            print(f"README updated: {readme.relative_to(WORKFLOWS_DIR.parent)}")

    for path in json_files:
        workflow = json.loads(path.read_text(encoding="utf-8"))
        changes = migrate_workflow(workflow)
        path.write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if changes["nodes"] or changes["renames"]:
            print(f"\n{path.relative_to(WORKFLOWS_DIR.parent)}")
            for item in changes["renames"]:
                print(f"  rename: {item}")
            for item in changes["nodes"]:
                print(f"  node: {item}")


if __name__ == "__main__":
    main()
