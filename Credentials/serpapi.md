# 🔍 คู่มือการขอ API Key จาก SerpApi (Google Search API)

SerpApi เป็นบริการที่ทำให้ AI Agent สามารถค้นหาข้อมูลจาก Google Search ได้แบบ Real-time ซึ่งเป็นเครื่องมือสำคัญที่ทำให้ AI ไม่จำกัดอยู่แค่ข้อมูลที่ถูกฝึกมา แต่สามารถหาข้อมูลล่าสุด (เช่น ข่าววันนี้, ราคาหุ้น, สถานการณ์ปัจจุบัน) ได้

---

## 🎯 ขั้นตอนที่ 1: สมัครสมาชิก SerpApi

1. ไปที่เว็บไซต์: [serpapi.com](https://serpapi.com/)
2. คลิกปุ่ม **"Sign Up"** (มุมขวาบน)
3. เลือกวิธีสมัคร:
   - **Google Account**: คลิกปุ่ม "Continue with Google" (แนะนำ - สะดวกที่สุด)
   - **Email**: กรอกอีเมลและรหัสผ่าน
4. รอระบบสร้างบัญชีและเข้าสู่ระบบอัตโนมัติ

---

## 🔑 ขั้นตอนที่ 2: ขอ API Key

เมื่อเข้าสู่ระบบแล้ว คุณจะอยู่ในหน้า Dashboard

1. ที่เมนูด้านซ้าย คลิกที่ **"Your API Key"**
2. คุณจะเห็น API Key ของคุณแสดงอยู่แล้ว (หน้าตาประมาณ `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)
3. คลิกปุ่ม **Copy** เพื่อคัดลอกคีย์เก็บไว้

> ⚠️ **คำเตือน:** ห้ามแชร์ API Key นี้กับผู้อื่น หรือนำไปใส่ในโค้ดที่อัปโหลดขึ้น GitHub เด็ดขาด

---

## 📊 ข้อมูลเกี่ยวกับ Free Tier (อัปเดต 2026)

บัญชีฟรีของ SerpApi มีข้อจำกัดดังนี้:
- **Searches**: **100 ครั้งต่อเดือน** (เพียงพอสำหรับการทดลองและเรียนรู้)
- **Real-time Results**: ผลลัพธ์ค้นหาจาก Google แบบเรียลไทม์
- **รองรับ**: Google Search, Google Images, Google Shopping, Google News
- **เหมาะสำหรับ**: ทดสอบ AI Agent ที่ต้องการข้อมูลล่าสุด

> **💡 คำแนะนำ:** ในชั้นเรียน แนะนำให้นักเรียนใช้ Search อย่างประหยัด (เช่น ทดสอบคำถาม 5-10 ครั้งต่อคน) เพื่อไม่ให้โควต้าหมดเร็วเกินไป

---

## 🔌 ขั้นตอนที่ 3: นำไปใส่ใน n8n

### วิธีที่ 1: ใช้กับ Node `SerpApi Tool` (แนะนำ - มี Node สำเร็จรูป)

1. ใน n8n ค้นหาและลาก Node **`SerpApi Tool`** มาวาง
2. ดับเบิลคลิกเพื่อเปิดการตั้งค่า
3. ที่ช่อง **Credential to connect with**
4. เลือก **Create New Credential**
5. หน้าต่างตั้งค่าจะให้กรอก:
   - **Credential Name**: เช่น `My SerpApi Free Key`
   - **API Key**: วางคีย์ที่ก๊อปปี้มาจากขั้นตอนที่ 2 ลงไป
6. กดปุ่ม **Save** เพื่อบันทึก

### วิธีที่ 2: ใช้กับ Node `HTTP Request` (ถ้าไม่มี Node สำเร็จรูป)

1. เพิ่ม Node `HTTP Request` ลงใน Workflow
2. ตั้งค่า:
   - **Method**: `GET`
   - **URL**: `https://serpapi.com/search.json`
   - **Authentication**: `None`
3. ในส่วน **Send Query Parameters**:
   - เพิ่ม Parameter:
     - Name: `api_key`
     - Value: `YOUR_SERPAPI_KEY` (แทนที่ด้วยคีย์จริง)
     - Name: `q`
     - Value: `{{$fromAI("query")}}` (AI จะส่งคำค้นหามาให้)
     - Name: `engine`
     - Value: `google`
4. กด Save

---

## 🎯 การใช้งานใน n8n (ตัวอย่าง Workflow)

**สถานการณ์ที่ AI Agent จะเรียกใช้ SerpApi:**
- "ราคาหุ้น Apple วันนี้เท่าไหร่?" → AI จะค้นหาข้อมูลล่าสุด
- "ข่าวเกี่ยวกับ AI วันนี้มีอะไรบ้าง?" → AI จะหาข่าวปัจจุบัน
- "สภาพอากาศที่กรุงเทพฯ ตอนนี้" → AI จะค้นหาข้อมูลสภาพอากาศล่าสุด

**การตั้งค่าใน AI Agent Node:**
1. ในส่วน **Tools** ของ AI Agent
2. เพิ่ม **SerpApi Tool** เข้าไป
3. ในส่วน **Description** ของ Tool:
   ```
   Call this tool to search for current information on Google. 
   Use this when the user asks about recent news, stock prices, 
   current events, or any information that changes frequently.
   ```

---

## 🛠️ ตัวอย่างการทดสอบ

เมื่อตั้งค่าเสร็จแล้ว ลองพิมพ์คำถามเหล่านี้ใน Chat Trigger:
1. `"ราคาหุ้น Tesla วันนี้เท่าไหร่?"`
2. `"ข่าวเกี่ยวกับ AI ล่าสุดมีอะไรบ้าง?"`
3. `"สภาพอากาศที่กรุงเทพฯ ตอนนี้เป็นยังไง?"`

AI ควรจะเรียกใช้ SerpApi เพื่อค้นหาข้อมูลล่าสุดและตอบกลับมาให้คุณได้

🎉 **เสร็จเรียบร้อย! ตอนนี้ AI Agent ของคุณสามารถค้นหาข้อมูลแบบ Real-time ได้แล้ว**
