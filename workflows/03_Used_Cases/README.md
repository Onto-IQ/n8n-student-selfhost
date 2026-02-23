# 03 - Use Cases จริงจากโลกธุรกิจ

โฟลเดอร์นี้รวบรวม Workflow ตัวอย่างจากโลกธุรกิจจริง ที่สามารถนำไปใช้งานได้ทันที

---

## 📚 รายการ Workflow

### ระดับพื้นฐาน (เริ่มต้น)

| ลำดับ | ไฟล์ | หัวข้อ | คำอธิบาย |
|-------|------|--------|----------|
| 01 | `01 - LINE Chat Gemini Model.json` | LINE Chat Bot | Chat Bot ที่ใช้ Google Gemini AI พร้อมความจำ |
| 02 | `02 - Form to Google Workspace & LINE.json` | Form Integration | ฟอร์มไป Google Sheets, Calendar, Docs, Drive และ LINE |

### ระดับกลาง (AI Powered)

| ลำดับ | ไฟล์ | หัวข้อ | คำอธิบาย |
|-------|------|--------|----------|
| 03 | `03 - Candidate Screening from Gmail.json` | HR Automation | AI คัดกรองใบสมัครจาก Gmail อัตโนมัติ |
| 04 | `04 - RAG with Pinecone (Load + Query).json` | RAG with Vector DB | AI อ่านเอกสารจาก Pinecone แล้วตอบคำถาม |

### ระดับสูง (Multi-Agent Systems)

| ลำดับ | ไฟล์ | หัวข้อ | คำอธิบาย |
|-------|------|--------|----------|
| 05A | `05A - Linear Multi-Agent Refund & Claim.json` | Linear Multi-Agent | Multi-Agent แบบเรียงลำดับ (Sequential) |
| 05B | `05B - Orchestration Multi-Agent Refund & Claim.json` | Orchestration Multi-Agent | Multi-Agent แบบ Orchestration ใช้ toolWorkflow |
| 05B-Sub | `05B-Sub-*.json` (4 ไฟล์) | Sub-Workflows | Sub-Workflows สำหรับ 05B |

---

## 🎯 รายละเอียดแต่ละ Workflow

### 01 - LINE Chat Gemini Model
**Chat Bot ที่ใช้ Google Gemini AI**

**องค์ประกอบ:**
- LINE Trigger: รับข้อความจาก LINE
- AI Agent + Google Gemini Chat Model
- Simple Memory: จำบทสนทนาได้

**ใช้งาน:**
1. สร้าง LINE Official Account
2. ตั้งค่า Webhook URL ใน LINE Developer
3. ใช้ ngrok หรือ Cloudflare Tunnel สำหรับ local testing

---

### 02 - Form to Google Workspace & LINE
**ระบบรับเรื่องครบวงจร**

**องค์ประกอบ:**
- Form Trigger: รับข้อมูลจากฟอร์ม
- Google Sheets: บันทึกข้อมูล
- Google Calendar: สร้างกิจกรรม
- Google Docs: สร้างเอกสาร
- Google Drive: จัดเก็บไฟล์
- LINE: แจ้งเตือน

**ใช้งาน:**
- ระบบรับเรื่อง
- การจอง/ลงทะเบียน
- CRM เบื้องต้น

**Credentials ที่ต้องใช้:**
- Google OAuth (Gmail, Sheets, Calendar, Drive, Docs)
- LINE Notify หรือ LINE Messaging API

---

### 03 - Candidate Screening from Gmail
**HR Automation - คัดกรองใบสมัคร**

**องค์ประกอบ:**
- Gmail Trigger: รับอีเมลที่มีคำว่า "สมัครงาน", "Resume", "CV"
- Google Drive: ดึง Job Description
- AI Agent: วิเคราะห์ Resume และให้คะแนน
- Google Sheets: บันทึกผลการคัดกรอง

**ใช้งาน:**
- HR รับใบสมัครอัตโนมัติ
- AI ให้คะแนนความเหมาะสม
- สร้าง Shortlist โดยอัตโนมัติ

**รองรับไฟล์:** PDF, TXT, DOCX

---

### 04 - RAG with Pinecone (Load + Query)
**AI อ่านเอกสารจาก Pinecone Vector DB**

**ส่วนที่ 1: Load Data (เตรียมข้อมูล)**
- ดึงเอกสารจาก Google Drive
- แปลงเป็น Vector ด้วย OpenAI Embeddings
- บันทึกลง Pinecone Vector Database

**ส่วนที่ 2: Query (ถามตอบ)**
- Chat Trigger รับคำถาม
- Vector Store Tool ค้นหาข้อมูลที่เกี่ยวข้อง
- AI Agent ตอบคำถามจากเอกสาร

**Pinecone Settings:**
- Index: n8n-demo-index
- Dimension: 1536 (text-embedding-3-small)

---

### 05A - Linear Multi-Agent Refund & Claim
**Multi-Agent แบบ Linear (Sequential Approach)**

**แนวคิด:** การทำงานแบบเรียงลำดับขั้นตอน ไม่มีการวนกลับ

**ขั้นตอน:**
1. Form Trigger: รับคำร้อง
2. Intent Classifier: วิเคราะห์ประเภทคำร้อง
3. Policy Validator: ตรวจสอบนโยบาย
4. Response Generator: ร่างคำตอบ
5. Send Gmail: ส่งอีเมลตอบกลับ

**ข้อดี:**
- ง่ายต่อการทำความเข้าใจ
- Debug ง่าย

**ข้อจำกัด:**
- หากข้อมูลผิดพลาดในกลางทาง ไม่สามารถย้อนกลับไปแก้ไขได้

---

### 05B - Orchestration Multi-Agent Refund & Claim
**Multi-Agent แบบ Orchestration (2026 Pattern)**

**แนวคิดปี 2026:** ใช้ AI Agent + toolWorkflow แทนการสร้าง Sub-Agents ซ้อนซ้อน

**สถาปัตยกรรม:**
```
Form Trigger
    ↓
Main AI Agent (Orchestrator)
    ↓ (เรียก Tools)
├→ toolWorkflow: Intent Classifier
├→ toolWorkflow: Policy Validator  
├→ toolWorkflow: Finance Calculator
└→ toolWorkflow: QA Reviewer
    ↓
Output Parser → IF Node → Gmail/LINE
    ↓ (ไม่ผ่าน)
  Note: Revision (จบ)
```

**ข้อดี:**
- ลดจาก 20+ nodes เหลือ ~12 nodes
- ไม่มี Code Node ซับซ้อน
- Sub-Workflows แยกจัดการง่าย
- ใช้ n8n 2.8.x Standard Pattern

### Sub-Workflows สำหรับ 05B

| ไฟล์ | หน้าที่ |
|------|--------|
| `05B-Sub-Intent-Classifier.json` | วิเคราะห์ประเภทคำร้อง |
| `05B-Sub-Policy-Validator.json` | ตรวจสอบนโยบายด้วย RAG |
| `05B-Sub-Finance-Calculator.json` | คำนวณเงินคืน/เคลม |
| `05B-Sub-QA-Reviewer.json` | ตรวจสอบคุณภาพคำตอบ |

---

## 🚀 วิธีใช้งาน

### Requirements
- n8n version **2.8.3** ขึ้นไป
- Credentials ตามแต่ละ Workflow:
  - OpenAI API Key (สำหรับ AI Agents)
  - Google OAuth (สำหรับ Google Workspace)
  - LINE API (สำหรับ LINE Bot)
  - Pinecone API (สำหรับ RAG)
  - Gmail OAuth (สำหรับ Candidate Screening)

### ขั้นตอนการเริ่มต้น

1. **Import Workflow:**
   - เปิด n8n
   - Import จากไฟล์ JSON

2. **ตั้งค่า Credentials:**
   - Settings → Credentials
   - เพิ่ม Credentials ที่จำเป็น

3. **Activate Workflow:**
   - Toggle "Active" เป็น ON
   - ทดสอบด้วย Test Data

---

## 📊 เปรียบเทียบ 05A vs 05B

| หัวข้อ | 05A Linear | 05B Orchestration |
|--------|------------|-------------------|
| **Pattern** | Sequential (เรียงลำดับ) | toolWorkflow (2026 Pattern) |
| **จำนวน Nodes** | ~20 nodes | ~12 nodes |
| **Code Node** | มี (ซับซ้อน) | ไม่มี |
| **Sub-Agents** | ซ้อนใน workflow เดียว | แยกเป็น Sub-Workflows |
| **State Manager** | มี (จัดการ state) | ไม่มี (Agent จัดการเอง) |
| **Loop Gatekeeper** | มี (ซับซ้อน) | ไม่มี (ใช้ IF Node) |
| **การ Debug** | ยาก | ง่าย (แยกไฟล์) |
| **การ Maintain** | ยาก | ง่าย |

---

## 💡 Key Concepts ใน Use Cases

| คำศัพท์ | คำอธิบาย |
|---------|----------|
| **RAG** | Retrieval Augmented Generation - AI อ่านเอกสารแล้วตอบ |
| **Vector DB** | ฐานข้อมูลแบบ Vector (เช่น Pinecone) |
| **Multi-Agent** | หลาย AI Agent ทำงานร่วมกัน |
| **Orchestration** | AI Agent หลักสั่งการ AI Agent ย่อย |
| **toolWorkflow** | เรียก workflow อื่นเป็นเครื่องมือ |
| **Sub-Workflow** | Workflow ย่อยที่ถูกเรียกใช้ |

---

## 🔗 การเชื่อมต่อกับ 02_AI_Agents_Basics

Workflow ในโฟลเดอร์นี้ต่อยอดจาก:
- `02 - AI Agent with Tools.json` → ใช้ Tools ใน 03, 05B
- `03 - Simple RAG with Memory.json` → ต่อยอดเป็น 04 (Pinecone)
- `04 - MCP Client.json` → แนวคิดเชื่อมต่อ External Services

---

## 📖 ต่อไปเรียนอะไร?

หลังจากจบโฟลเดอร์นี้:
1. ลองปรับแต่ง Workflow ตาม use case ของคุณ
2. สร้าง Multi-Agent ระบบของตัวเอง
3. เรียนรู้การ Deploy บน Production
