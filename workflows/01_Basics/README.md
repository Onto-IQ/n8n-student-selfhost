# 01 - พื้นฐาน n8n (Basics)

โฟลเดอร์นี้รวบรวม Workflow พื้นฐานสำหรับผู้เริ่มต้นเรียนรู้ n8n ก่อนไปใช้งาน AI Agents

---

## 📚 รายการ Workflow

| ลำดับ | ไฟล์ | หัวข้อ | คำอธิบาย |
|-------|------|--------|----------|
| 01 | `01-Learn-JSON-Basics.json` | JSON พื้นฐาน | เรียนรู้ Key-Value Pair, Data Types (String, Number, Boolean, Array, Object, Null) |
| 02 | `02-Flow-Control-Demo.json` | Flow Control - IF/Switch | สาธิตการใช้ IF Node และ Switch Node แยกกรณี |
| 03 | `03-Flow-Control-Demo-Loop.json` | Flow Control - Loop | สาธิตการใช้ Loop Node และ Item Lists วนซ้ำข้อมูล |
| 04 | `04-Data-Transformation.json` | Data Transformation | แปลงข้อมูลด้วย Edit Fields (Set) และ Code Node |
| 05 | `05-Working-with-External-APIs.json` | External APIs | เรียนรู้ GET/POST Request และ Authentication |
| 06 | `06-Webhooks-and-Triggers.json` | Webhooks & Triggers | เปิดรับข้อมูลจากภายนอกด้วย Webhook Node |

---

## 🎯 แนวทางการเรียน

เรียนตามลำดับตั้งแต่ 01 → 06 เพราะแต่ละบทสะสมความรู้ไปเรื่อยๆ

### บทที่ 1: JSON Basics (ทุกอย่างเริ่มจากตรงนี้)
- ทำไม n8n ถึงใช้ JSON เป็นภาษาหลัก
- Key-Value Pair คืออะไร
- Data Types: String, Number, Boolean, Array, Object, Null

### บทที่ 2: Flow Control - IF/Switch (สาขาและเงื่อนไข)
- IF Node: ตรวจสอบเงื่อนไข (VIP หรือไม่?)
- Switch Node: แยกกรณีตามคะแนน (A/B/C/F)
- Merge Node: รวมผลลัพธ์จากหลายทาง

### บทที่ 3: Flow Control - Loop (วนซ้ำ)
- Item Lists: แยก Array เป็นรายบุคคล
- Loop Node: วนทำงานทีละรายการ
- Set Node: ประมวลผลแต่ละรายการ

### บทที่ 4: Data Transformation (แปลงข้อมูล)
- Edit Fields (Set): เปลี่ยนชื่อฟิลด์, คัดกรองข้อมูล
- Code Node: JavaScript สำหรับข้อมูลซับซ้อน

### บทที่ 5: External APIs (เชื่อมต่อภายนอก)
- GET Request: ดึงข้อมูล (เช่น สภาพอากาศ)
- POST Request: ส่งข้อมูล (เช่น LINE, Slack)
- Authentication: API Key, Bearer Token

### บทที่ 6: Webhooks (รอรับข้อมูล)
- Webhook Node: เปิดประตูรับข้อมูลจากภายนอก
- Response Mode: ตอบกลับทันทีหรือรอจบ Workflow

---

## 🚀 วิธีใช้งาน

1. เปิด n8n (เวอร์ชัน 2.8.3 ขึ้นไป)
2. สร้าง Workflow ใหม่
3. Copy-Paste เนื้อหาจากไฟล์ JSON หรือใช้ **Import from File**
4. อ่าน Sticky Notes ตามลำดับที่ให้ไว้
5. กด **Test step** ทีละ Node เพื่อดูผลลัพธ์

---

## ⚙️ Requirements

- n8n version **2.8.3** ขึ้นไป
- ไม่ต้องใช้ API Key สำหรับบทเรียนพื้นฐาน (ยกเว้นบทที่ 5)

---

## 💡 Tips

- **Sticky Notes สีต่างๆ:**
  - 🟣 สีม่วง = บทนำ (Overview)
  - 🟢 สีเขียว = ขั้นตอนที่ 1
  - 🔵 สีฟ้า = ขั้นตอนที่ 2
  - 🟠 สีส้ม = ขั้นตอนที่ 3
  - 🔴 สีแดง = คำเตือน หรือ จุดสิ้นสุด
