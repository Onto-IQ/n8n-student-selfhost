# 🔄 คู่มือการขอ API Key จาก OpenRouter

OpenRouter เป็น "ศูนย์รวม" โมเดล AI จากหลายๆ ค่าย (เช่น Claude จาก Anthropic, Llama จาก Meta, หรือแม้แต่ GPT จาก OpenAI) รวมไว้ที่เดียว ข้อดีคือ **สมัครครั้งเดียว ใช้ได้ทุกค่าย** และมีโมเดลฟรีให้เลือกใช้ด้วย

---

## 🎯 ขั้นตอนที่ 1: สมัครสมาชิก OpenRouter

1. ไปที่เว็บไซต์: [openrouter.ai](https://openrouter.ai/)
2. คลิกปุ่ม **"Sign In"** (มุมขวาบน)
3. เลือกล็อกอินด้วยบัญชี Google (Gmail) หรือบัญชีอื่นๆ ตามสะดวก
4. เมื่อล็อกอินสำเร็จ คุณจะเข้ามาที่หน้า Dashboard

---

## 💰 ขั้นตอนที่ 2: เติมเครดิต (ทางเลือก - หากต้องการใช้รุ่นเสียเงิน)

หากคุณต้องการใช้เฉพาะโมเดลที่มีคำว่า "Free" กำกับ (เช่น `meta-llama/llama-3.1-8b-instruct:free`) คุณสามารถข้ามขั้นตอนนี้ไปได้เลย

1. ที่เมนูด้านซ้าย เลือก **"Settings"** > **"Credits"**
2. คลิกปุ่ม **"Add Credits"**
3. เลือกจำนวนเงินที่ต้องการเติม (เริ่มต้นมักจะอยู่ที่ $5)
4. กรอกข้อมูลบัตรเครดิต/เดบิต และทำการชำระเงินให้เรียบร้อย

---

## 🔑 ขั้นตอนที่ 3: สร้าง API Key

1. ที่เมนูด้านซ้าย ไปที่หัวข้อ **"Keys"** (หรือเข้าที่ [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys))
2. คลิกปุ่ม **"Create Key"**
3. ตั้งชื่อคีย์ (Name) เช่น `n8n Router Key`
4. (Optional) คุณสามารถกำหนด **Credit Limit** สำหรับคีย์นี้ได้ (เช่น จำกัดไม่ให้คีย์นี้ใช้เงินเกิน $1) เพื่อความปลอดภัย
5. กดปุ่ม **"Create"**
6. ⚠️ หน้าต่างป๊อปอัปจะแสดง API Key ของคุณ (หน้าตาประมาณ `sk-or-v1-...`)
   - **สำคัญมาก:** ก๊อปปี้คีย์นี้เก็บไว้ในที่ปลอดภัยทันที เพราะระบบจะไม่แสดงคีย์เต็มๆ ให้ดูอีก

> 🚨 **ข้อควรระวัง:** ห้ามนำ API Key ไปใส่ในโค้ดดิบๆ หรืออัปโหลดขึ้นแหล่งเก็บโค้ดสาธารณะ (เช่น GitHub) เด็ดขาด

---

## 🔌 ขั้นตอนที่ 4: นำไปตั้งค่าใน n8n

การใช้ OpenRouter ใน n8n มักจะทำผ่าน `HTTP Request` Node หรือหาก n8n เวอร์ชั่นของคุณรองรับ สามารถใช้ผ่าน Node ของ Langchain ได้ (มักจะตั้งค่าให้มอง OpenRouter เป็น OpenAI-compatible API)

### วิธีที่ 1: ใช้กับ Node `HTTP Request` (วิธีมาตรฐาน)

1. เพิ่ม Node `HTTP Request` ลงใน Workflow
2. เปิดตั้งค่า Node
   - **Method**: `POST`
   - **URL**: `https://openrouter.ai/api/v1/chat/completions`
   - **Authentication**: เลือก `None`
3. ในส่วน **Send Headers** (ต้องเปิดสวิตช์):
   - เพิ่ม Header ใหม่:
     - Name: `Authorization`
     - Value: `Bearer <YOUR_OPENROUTER_API_KEY>` (แทนที่ `<YOUR_OPENROUTER_API_KEY>` ด้วยคีย์ที่คุณก๊อปปี้มา)
   - เพิ่ม Header ใหม่ (แนะนำ):
     - Name: `HTTP-Referer`
     - Value: `https://n8n.your-domain.com` (ใส่ URL ของ n8n คุณ)
     - Name: `X-Title`
     - Value: `n8n Student App`
4. ในส่วน **Send Body** (ต้องเปิดสวิตช์):
   - Body Content Type: `JSON`
   - ใส่ข้อมูล JSON (ตัวอย่าง):
     ```json
     {
       "model": "meta-llama/llama-3.1-8b-instruct:free",
       "messages": [
         {"role": "user", "content": "What is the capital of France?"}
       ]
     }
     ```

### วิธีที่ 2: ใช้กับ Node `OpenAI Chat Model` (แบบระบุ Base URL)

*เนื่องจาก API ของ OpenRouter ออกแบบมาให้เหมือนกับ OpenAI คุณจึงสามารถใช้ Node ของ OpenAI ได้เลย!*

1. เพิ่ม Node `OpenAI Chat Model` ลงใน Workflow
2. ในช่อง **Credential to connect with** ให้สร้าง Credential ใหม่ (เลือก `OpenAI API`)
   - ตั้งชื่อ Credential เช่น `My OpenRouter Key`
   - ช่อง API Key: ใส่คีย์ OpenRouter (ที่ขึ้นต้นด้วย `sk-or-v1-...`) ของคุณ
   - กด Save และปิดหน้าต่าง
3. กลับมาที่ตั้งค่าของ Node `OpenAI Chat Model`
   - **Model**: ระบบอาจจะดึงรายชื่อ Model ของ OpenAI มา (เช่น gpt-4o) **ไม่ต้องสนใจ** ให้พิมพ์ชื่อโมเดลของ OpenRouter ทับลงไปเลย เช่น `meta-llama/llama-3.1-8b-instruct:free` (พิมพ์เสร็จให้กด Enter)
4. เลื่อนลงมาด้านล่าง หาหัวข้อ **Options** หรือ **Additional Parameters**
   - มองหาและเปิดใช้ **Base URL**
   - เปลี่ยน URL เป็น: `https://openrouter.ai/api/v1`

🎉 **เสร็จเรียบร้อย! คุณสามารถใช้โมเดลฟรีๆ มากมายจาก OpenRouter ใน n8n ได้แล้ว**
