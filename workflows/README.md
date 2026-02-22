# 🎓 n8n Educational Workflows

โฟลเดอร์นี้รวบรวม Workflow พื้นฐานสำหรับการเรียนการสอน (Educational Workflows) สำหรับผู้เริ่มต้นใช้งาน n8n

---

## 📂 โครงสร้างโฟลเดอร์

```
workflows/
├── 01_Basics/                    # พื้นฐาน n8n (JSON, Flow Control, Data Transform)
│   ├── 01-Learn-JSON-Basics.json
│   ├── 02-Flow-Control-Demo-IF-Switch.json
│   ├── 03-Flow-Control-Demo-Loop.json
│   ├── 04-Data-Transformation.json
│   ├── 05-Working-with-External-APIs.json
│   └── 06-Webhooks-and-Triggers.json
│
├── 02_AI_Agents_Basics/          # AI Agent พื้นฐาน
│   ├── 01-Simple-AI-Agent.json
│   └── 02-AI-Agent-with-Tools.json
│
├── 03_Used_Cases/                # Use Cases จริง
│   └── 03 - LINE Chat Gemini Model.json
│
└── README.md                     # ไฟล์นี้
```

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

## � หมายเหตุ

- ทุก Workflow มี Sticky Notes ภาษาไทยสำหรับอธิบายแต่ละ Node
- Workflows ทดสอบและรองรับ n8n เวอร์ชัน **2.8.3** ขึ้นไป
- อ่านคำอธิบายจาก Sticky Notes ตามลำดับหมายเลข และลองกด **Test step** ทีละ Node
