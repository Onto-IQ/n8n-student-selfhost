# 🎓 n8n Educational Workflows

โฟลเดอร์นี้รวบรวม Workflow สำหรับการเรียนการสอน (Educational Workflows) สำหรับผู้เริ่มต้นใช้งาน n8n จนถึงระดับกลาง-สูง

---

## 📂 โครงสร้างโฟลเดอร์

```
workflows/
├── 01_Basics/                    # พื้นฐาน n8n (สำหรับมือใหม่)
│   ├── 01-Learn-JSON-Basics.json
│   ├── 02-Flow-Control-Demo.json
│   ├── 03-Flow-Control-Demo-Loop.json
│   ├── 04-Data-Transformation.json
│   ├── 05-Working-with-External-APIs.json
│   └── 06-Webhooks-and-Triggers.json
│
├── 02_AI_Agents_Basics/          # AI Agent พื้นฐาน
│   ├── 01 - Basic Chat Agent & Memory.json
│   ├── 02 - AI Agent with Tools.json
│   ├── 03 - Simple RAG with Memory.json
│   ├── 04 - MCP Client.json
│   └── 04 - MCP Server.json
│
├── 03_Used_Cases/                # Use Cases จริงจากโลกธุรกิจ
│   ├── 01 - LINE Chat Gemini Model.json
│   ├── 02 - Form to Google Workspace & LINE.json
│   ├── 03 - Candidate Screening from Gmail.json
│   ├── 04 - RAG with Pinecone (Load + Query).json
│   ├── 05A - Linear Multi-Agent Refund & Claim.json
│   ├── 05B - Orchestration Multi-Agent Refund & Claim.json
│   ├── 05B-Sub-Intent-Classifier.json
│   ├── 05B-Sub-Policy-Validator.json
│   ├── 05B-Sub-Finance-Calculator.json
│   └── 05B-Sub-QA-Reviewer.json
│
└── README.md                     # ไฟล์นี้
```

---

## 🎯 แนวทางการเรียน

### Phase 1: พื้นฐาน n8n (01_Basics)
สำหรับผู้ที่ไม่เคยใช้ n8n มาก่อน
- เรียนรู้ JSON พื้นฐาน
- Flow Control (IF, Switch, Loop)
- Data Transformation
- External APIs และ Webhooks

### Phase 2: AI Agents (02_AI_Agents_Basics)
เริ่มสร้าง AI Agents ที่สามารถคิดและใช้เครื่องมือได้
- Basic Chat Agent + Memory
- AI Agent with Tools (Function Calling)
- RAG (AI อ่านเอกสารแล้วตอบ)
- MCP (Model Context Protocol)

### Phase 3: Use Cases จริง (03_Used_Cases)
ตัวอย่างจากโลกธุรกิจที่ใช้งานจริงได้
- LINE Chat Bot with Gemini
- Form to Google Workspace
- Candidate Screening
- Multi-Agent Refund & Claim

---

## 🚀 วิธีนำเข้า Workflow

### วิธีที่ 1: Copy-Paste (เร็วที่สุด)

1. เปิดหน้า n8n (`https://n8n.yourdomain.com`)
2. สร้าง Workflow ใหม่ (**+ Add Workflow**)
3. เปิดไฟล์ `.json` ที่ต้องการ
4. คัดลอกทั้งหมด (`Ctrl+A` → `Ctrl+C`)
5. วางใน n8n (`Ctrl+V`)

### วิธีที่ 2: Import ผ่าน Menu

1. ใน n8n กด **Workflow** → **Import from File**
2. เลือกไฟล์ `.json` จากโฟลเดอร์
3. กด **Save**

### วิธีที่ 3: Import ผ่าน URL (ถ้าใช้ GitHub)

1. เปิดไฟล์ `.json` ใน GitHub
2. กด **Raw** เพื่อดู URL
3. ใน n8n: **Workflow** → **Import from URL**
4. วาง URL และกด Import

---

## 📋 รายการ Workflow ทั้งหมด

### 01_Basics - พื้นฐาน
| ไฟล์ | หัวข้อ |
|------|--------|
| 01-Learn-JSON-Basics.json | JSON พื้นฐาน |
| 02-Flow-Control-Demo.json | IF และ Switch Node |
| 03-Flow-Control-Demo-Loop.json | Loop และ Item Lists |
| 04-Data-Transformation.json | Edit Fields และ Code Node |
| 05-Working-with-External-APIs.json | HTTP Request GET/POST |
| 06-Webhooks-and-Triggers.json | Webhook Node |

### 02_AI_Agents_Basics - AI Agents
| ไฟล์ | หัวข้อ |
|------|--------|
| 01 - Basic Chat Agent & Memory.json | AI Agent + Window Buffer Memory |
| 02 - AI Agent with Tools.json | Agent พร้อมเครื่องมือ (Tools) |
| 03 - Simple RAG with Memory.json | RAG อ่านเอกสารแล้วตอบ |
| 04 - MCP Client.json | เชื่อมต่อใช้ Tools จากภายนอก |
| 04 - MCP Server.json | เปิด n8n เป็น Server |

### 03_Used_Cases - Use Cases จริง
| ไฟล์ | หัวข้อ |
|------|--------|
| 01 - LINE Chat Gemini Model.json | LINE Bot ใช้ Gemini AI |
| 02 - Form to Google Workspace & LINE.json | Form ไป Sheets, Calendar, Drive |
| 03 - Candidate Screening from Gmail.json | AI คัดกรองใบสมัครจาก Gmail |
| 04 - RAG with Pinecone.json | RAG ใช้ Pinecone Vector DB |
| 05A - Linear Multi-Agent Refund & Claim.json | Multi-Agent แบบ Linear |
| 05B - Orchestration Multi-Agent Refund & Claim.json | Multi-Agent แบบ Orchestration |
| 05B-Sub-*.json | Sub-Workflows สำหรับ 05B |

---

## ⚙️ Requirements

- n8n เวอร์ชัน **2.8.3** ขึ้นไป
- OpenAI API Key (สำหรับ AI Agents)
- LINE API (สำหรับ LINE Chat)
- Google OAuth (สำหรับ Google Workspace)
- Pinecone API (สำหรับ RAG with Pinecone)

---

## 📝 หมายเหตุ

- ทุก Workflow มี Sticky Notes ภาษาไทยสำหรับอธิบายแต่ละ Node
- Workflows ทดสอบและรองรับ n8n เวอร์ชัน **2.8.3** ขึ้นไป
- อ่านคำอธิบายจาก Sticky Notes ตามลำดับหมายเลข
- ลองกด **Test step** ทีละ Node เพื่อดูผลลัพธ์

---

## 📖 อ่านเพิ่มเติม

- [01_Basics/README.md](01_Basics/README.md) - รายละเอียดพื้นฐาน n8n
- [02_AI_Agents_Basics/README.md](02_AI_Agents_Basics/README.md) - รายละเอียด AI Agents
- [03_Used_Cases/README.md](03_Used_Cases/README.md) - รายละเอียด Use Cases จริง

---

## 🗺️ แผนผังการเรียน (Learning Path)

```
🌱 เริ่มต้น                    🚀 ระดับกลาง                 🎯 ระดับสูง
    │                             │                            │
    ▼                             ▼                            ▼
┌─────────────┐            ┌─────────────┐            ┌─────────────┐
│ 01_Basics   │     →      │ 02_AI_Agents│     →      │ 03_Use_Cases│
│             │            │ _Basics     │            │             │
├─────────────┤            ├─────────────┤            ├─────────────┤
│ • JSON      │            │ • AI Agent  │            │ • LINE Bot  │
│ • Flow      │            │ • Memory    │            │ • RAG + DB  │
│   Control   │            │ • Tools     │            │ • Multi-    │
│ • API       │            │ • RAG       │            │   Agent     │
│ • Webhook   │            │ • MCP       │            │             │
└─────────────┘            └─────────────┘            └─────────────┘
     │                            │                            │
     └────────────────────────────┴────────────────────────────┘
                                    │
                                    ▼
                        ┌─────────────────────┐
                        │   🎓 สร้าง Workflow  │
                        │     ของตัวเอง!      │
                        └─────────────────────┘
```

**ระยะเวลาแนะนำ:**
- Phase 1: 1-2 วัน (6 workflow)
- Phase 2: 2-3 วัน (5 workflow)
- Phase 3: 3-5 วัน (7 workflow + ทดสอบปรับแต่ง)
