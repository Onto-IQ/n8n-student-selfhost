# 02 - AI Agents พื้นฐาน (AI Agents Basics)

โฟลเดอร์นี้รวบรวม Workflow สำหรับเรียนรู้การสร้าง AI Agents ตั้งแต่พื้นฐานจนถึงระดับกลาง

---

## 📚 รายการ Workflow

| ลำดับ | ไฟล์ | หัวข้อ | คำอธิบาย |
|-------|------|--------|----------|
| 01 | `01 - Basic Chat Agent & Memory.json` | AI Agent + Memory พื้นฐาน | สร้าง Chat Agent พร้อม Window Buffer Memory |
| 02 | `02 - AI Agent with Tools.json` | AI Agent + Tools | Agent ที่ใช้เครื่องมือภายนอก (Calculator, Wikipedia, Weather) |
| 03 | `03 - Simple RAG with Memory.json` | RAG (Retrieval Augmented Generation) | AI Agent ที่อ่านเอกสารแล้วตอบคำถามได้ |
| 04 | `04 - MCP Client.json` | MCP Client | Agent เชื่อมต่อใช้ Tools จาก MCP Server ภายนอก |
| 04 | `04 - MCP Server.json` | MCP Server | เปิด n8n เป็น MCP Server ให้ AI อื่นใช้ Tools |

---

## 🎯 แนวทางการเรียน

เรียนตามลำดับตั้งแต่ 01 → 04 เพื่อสะสมความรู้แบบ step-by-step

### บทที่ 1: Basic Chat Agent & Memory
**หัวใจของ AI Agent:**
- AI Agent Node: ตัวสั่งการหลัก (สมองส่วนควบคุม)
- Language Model (LLM): สมองส่วนคิด (OpenAI GPT-4o-mini)
- Window Buffer Memory: ความจำระยะสั้น (จำบทสนทนาได้)

**ทดสอบ:**
1. พิมพ์ "ฉันชื่อสมชาย"
2. ถามต่อ "ฉันชื่ออะไร?"
3. AI จะจำชื่อคุณได้เพราะมี Memory

---

### บทที่ 2: AI Agent with Tools
**AI ที่ใช้เครื่องมือได้ (Function Calling):**
- Calculator Tool: คำนวณเลข
- Wikipedia Tool: ค้นหาข้อมูลทั่วไป
- Weather API Tool: ดูสภาพอากาศ

**วิธีทดสอบ:**
- "จองห้องประชุมพรุ่งนี้ บ่าย 2 โมง"
- "ส่งอีเมลหาทีมบอกว่าประชุมเสร็จแล้ว"
- "คำนวณ 125 * 48 ให้หน่อย"

---

### บทที่ 3: Simple RAG with Memory
**AI ที่อ่านเอกสารแล้วตอบคำถาม:**
- **Data Load Flow:** โหลดไฟล์ PDF → แยกเป็นช่วง → สร้าง Vector
- **Retriever Flow:** รับคำถาม → ค้นหา Vector ที่ใกล้เคียง → ตอบคำถาม

**องค์ประกอบ:**
- Embeddings OpenAI: แปลงข้อความเป็นตัวเลข (Vector)
- Vector Store: คลังเก็บ Vector
- Data Loader: โหลดไฟล์ PDF
- Text Splitter: แบ่งเอกสารเป็นช่วงเล็กๆ

---

### บทที่ 4: MCP (Model Context Protocol)

#### MCP Client (ใช้ Tools จากภายนอก)
**แนวคิด:** AI Agent เราไม่ต้องสร้าง Tools เอง แต่เชื่อมต่อไปยัง MCP Server ภายนอก

**เปรียบเสมือน:** แทนที่จะซื้อรถคันใหม่ เราใช้บริการ Grab แทน

**ใช้งาน:**
- AI Agent ใช้ Chat Trigger
- MCP Client เชื่อมต่อไปยัง Server ภายนอก
- Server มี Tools: Calculator, Gmail, Calendar

#### MCP Server (ให้ AI อื่นใช้ Tools ของเรา)
**แนวคิด:** กลับด้านจาก MCP Client
- เราสร้าง Tools ใน n8n
- เปิดเป็น MCP Server
- AI ภายนอกเชื่อมต่อมาใช้

**เปรียบเสมือน:** เราเป็นโรงงานผลิตอาหาร ส่งให้ร้านอื่นขาย

**องค์ประกอบ:**
- MCP Trigger: รอ AI ภายนอกเชื่อมต่อ
- Tools: Calculator, Gmail, Calendar

---

## 🚀 วิธีใช้งาน

### Requirements
- n8n version **2.28.6** ขึ้นไป
- OpenAI API Key (สำหรับทุกบทยกเว้น MCP Server)

### ขั้นตอนการเริ่มต้น

1. **ตั้งค่า OpenAI Credentials:**
   - ไปที่ Settings → Credentials
   - เพิ่ม OpenAI API Key

2. **Import Workflow:**
   - เปิด n8n
   - สร้าง Workflow ใหม่
   - Import จากไฟล์ JSON

3. **ทดสอบ:**
   - คลิกปุ่ม **Chat** ที่มุมซ้ายล่าง
   - หรือกด **Test step** ทีละ Node

---

## 💡 Key Concepts

| คำศัพท์ | คำอธิบาย |
|---------|----------|
| **Agent** | AI ที่สามารถคิดและตัดสินใจได้ |
| **LLM** | Large Language Model (เช่น GPT-4o) |
| **Memory** | ความจำที่ให้ AI จำบทสนทนาก่อนหน้า |
| **Tools** | เครื่องมือที่ AI ใช้ได้ (Calculator, API) |
| **RAG** | Retrieval Augmented Generation - AI อ่านเอกสารแล้วตอบ |
| **Vector** | ตัวเลขที่แทนข้อความ (ใช้ค้นหาความคล้าย) |
| **MCP** | Model Context Protocol - มาตรฐานเชื่อม AI กับ Tools |

---

## 🔗 Connection Types ใน AI Agent

```
AI Agent Node
    ├─ ai_languageModel ──→ LLM (OpenAI, Anthropic)
    ├─ ai_memory ─────────→ Memory (Buffer, Window)
    ├─ ai_tool ───────────→ Tools (Calculator, API)
    └─ ai_outputParser ───→ Output Parser (JSON Schema)
```

---

## 📖 ต่อไปเรียนอะไร?

หลังจากจบโฟลเดอร์นี้ ไปต่อที่:
- `03_Used_Cases/` - Use Cases จริงจากโลกธุรกิจ
- ตัวอย่าง: LINE Chat Bot, Form Processing, Candidate Screening, RAG with Pinecone
