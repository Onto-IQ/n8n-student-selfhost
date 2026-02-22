# 🌲 คู่มือการขอ API Key จาก Pinecone (Vector Database)

Pinecone เป็นบริการ Vector Database ที่ได้รับความนิยมสูงสุดสำหรับการทำ **RAG (Retrieval-Augmented Generation)** โดยเฉพาะในหลักสูตรสอน AI ทั่วโลก ทำให้ AI สามารถจำข้อมูลระยะยาวได้ (Long-term Memory) และมี Free Tier ที่เพียงพอสำหรับการเรียนรู้

---

## 🎯 ขั้นตอนที่ 1: สมัครสมาชิก Pinecone

1. ไปที่เว็บไซต์: [pinecone.io](https://pinecone.io/)
2. คลิกปุ่ม **"Start Free"** (มุมขวาบน)
3. กรอกข้อมูลการสมัคร:
   - **Email**: ใส่อีเมลของคุณ
   - **Password**: ตั้งรหัสผ่านที่ปลอดภัย
   - **Company/Organization**: ใส่ชื่อองค์กรหรือ "Personal" ก็ได้
4. กด **Sign Up**
5. รอรับอีเมลยืนยันและคลิกลิงก์เพื่อยืนยันบัญชี

---

## 🏠 ขั้นตอนที่ 2: สร้าง Project และ Index

เมื่อล็อกอินเข้ามาแล้ว คุณจะอยู่ในหน้า Dashboard

1. **สร้าง Project** (ถ้ายังไม่มี):
   - ที่แถบด้านบน คลิก **"New Project"**
   - ตั้งชื่อ Project เช่น `n8n-rag-course`
   - เลือก Region ที่ใกล้คุณที่สุด (เช่น `us-east-1`)
   - กด **Create Project**

2. **สร้าง Index** (ที่เก็บข้อมูล Vector):
   - ใน Project ที่เพิ่งสร้าง คลิกปุ่ม **"Create Index"**
   - ตั้งค่าดังนี้ (แนะนำสำหรับการเรียนรู้):
     - **Index name**: `n8n-demo-index`
     - **Dimension**: `1536` (สำหรับ OpenAI embeddings ที่นิยมที่สุด)
     - **Metric**: `cosine` (วัดความคล้ายคลึงของข้อมูล)
     - **Pod type**: เลือก `p1.x1` (เป็นแบบ Serverless ในรุ่นใหม่)
   - กด **Create**
   - รอระบบสร้าง Index สักครู่ (ประมาณ 1-2 นาที)

---

## 🔑 ขั้นตอนที่ 3: ขอ API Key

1. ที่เมนูด้านซ้าย คลิกที่ **"API Keys"**
2. คลิกปุ่ม **"Create API Key"**
3. ตั้งชื่อคีย์ (Name) เช่น `n8n-course-key`
4. กด **Create**
5. ⚠️ **สำคัญมาก:** หน้าต่างป๊อปอัปจะแสดง API Key ของคุณ (หน้าตาประมาณ `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)
   - **คุณจะเห็นคีย์นี้เพียงครั้งเดียวเท่านั้น!**
   - กดปุ่ม **Copy** เก็บไว้ในที่ปลอดภัยทันที

> 🚨 **คำเตือน:** ห้ามส่ง API Key ให้คนอื่น หรืออัปโหลดขึ้น GitHub หาก Pinecone ตรวจพบการใช้งานผิดปกติ บัญชีอาจถูกระงับได้

---

## 📊 ข้อมูลเกี่ยวกับ Free Tier (อัปเดต 2026)

บัญชีฟรีของ Pinecone มีข้อจำกัดดังนี้:
- **Index**: สามารถสร้างได้ **1 Index** เท่านั้น (เพียงพอสำหรับการเรียนรู้)
- **Pods**: ใช้งานได้ **1 Pod** แบบ Serverless
- **Monthly Active Records**: ประมาณ 100,000 records (เก็บข้อมูลได้มากพอสำหรับคู่มือหรือเอกสาร)
- **ความจุ**: แต่ละ Index สามารถเก็บข้อมูลได้ประมาณ 2-5 MB (ขึ้นอยู่กับขนาดของ Vector)
- **เหมาะสำหรับ**: เก็บคู่มือ, เอกสาร, ความรู้ทั่วไป ไม่เหมาะสำหรับข้อมูลขนาดใหญ่เช่นทั้งเว็บไซต์

---

## 🔌 ขั้นตอนที่ 4: นำไปใส่ใน n8n

1. กลับมาที่ n8n ของคุณ
2. เพิ่ม Node ที่เกี่ยวข้องกับ Vector Store เช่น:
   - `Pinecone Vector Store` (อยู่ในหมวด Advanced AI)
3. ดับเบิลคลิกเพื่อเปิดการตั้งค่า Node
4. ที่ช่อง **Credential to connect with**
5. เลือก **Create New Credential**
6. หน้าต่างตั้งค่าจะให้กรอก:
   - **Credential Name**: เช่น `My Pinecone Free Tier`
   - **API Key**: วางคีย์ที่ก๊อปปี้มาจากขั้นตอนที่ 3 ลงไป
   - **Environment**: เลือก `us-east-1` (หรือ Region ที่คุณสร้าง Index ไว้)
7. กดปุ่ม **Save** เพื่อบันทึก

---

## 🎯 การใช้งานใน n8n (ตัวอย่าง Workflow)

**สถานการณ์ทั่วไปที่จะใช้ Pinecone:**
1. **Document Loading**: ใช้ `Document Loader` อ่านไฟล์ PDF/Word/Text
2. **Text Splitting**: ใช้ `Text Splitter` แบ่งข้อความเป็นชิ้นๆ (Chunks)
3. **Embedding**: ใช้ `OpenAI Embeddings` แปลงข้อความเป็น Vector
4. **Store**: ใช้ `Pinecone Vector Store` เก็บ Vector ลงฐานข้อมูล
5. **Retrieve**: ใช้ `Vector Store Retriever` ค้นหาข้อมูลที่เกี่ยวข้อง
6. **Generate**: ใช้ `AI Agent` ตอบคำถามโดยอิงจากข้อมูลที่ดึงมา

🎉 **เสร็จเรียบร้อย! ตอนนี้ AI Agent ของคุณมีความจำระยะยาวแล้ว**
