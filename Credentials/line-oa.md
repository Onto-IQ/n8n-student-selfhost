# 💬 คู่มือการขอ API Key จาก LINE Official Account (Messaging API)

LINE Messaging API ช่วยให้ n8n ของคุณสามารถส่งและรับข้อความผ่าน LINE Official Account (LINE OA) ได้ ซึ่งเหมาะมากสำหรับการสร้าง Chatbot หรือระบบแจ้งเตือน (Notification)

---

## 📱 ขั้นตอนที่ 1: สมัครและสร้าง Provider ใน LINE Developers

1. ไปที่เว็บไซต์: [LINE Developers Console](https://developers.line.biz/console/)
2. ล็อกอินด้วยบัญชี LINE ของคุณ
3. (หากเพิ่งเคยใช้ครั้งแรก) ระบบจะให้คุณสร้าง **Developer Account** กรอกชื่อและอีเมลให้เรียบร้อย
4. เมื่อเข้ามาที่ Console แล้ว ให้ดูที่เมนูด้านซ้ายใต้คำว่า **Providers**
5. คลิกปุ่ม **"Create"** (หรือปุ่ม + หากมี Provider อยู่แล้ว) เพื่อสร้าง Provider ใหม่ (เปรียบเสมือนโฟลเดอร์จัดเก็บแอปของคุณ)
6. ตั้งชื่อ Provider (เช่น `n8n Student Projects`) แล้วกด **Create**

---

## 🤖 ขั้นตอนที่ 2: สร้าง Messaging API Channel

1. ภายใน Provider ที่เพิ่งสร้าง คลิกเลือก **"Create a new channel"**
2. เลือกประเภทเป็น **"Messaging API"**
3. กรอกข้อมูลรายละเอียดของ Channel (ข้อมูลเหล่านี้จะไปแสดงเป็นชื่อและรูปโปรไฟล์ของ LINE OA ของคุณ):
   - **Channel name**: ชื่อบอท (เช่น `My n8n Bot`)
   - **Channel description**: คำอธิบายสั้นๆ (เช่น `บอททดสอบ n8n`)
   - **Category & Subcategory**: เลือกหมวดหมู่ที่เหมาะสม
   - **Email address**: ใส่อีเมลของคุณ
4. ติ๊กถูกยอมรับเงื่อนไข (Terms of Use) ทั้งสองข้อด้านล่างสุด
5. กดปุ่ม **Create** และยืนยัน (OK) อีกครั้ง

---

## 🔑 ขั้นตอนที่ 3: ขอ Channel Access Token (สำคัญ!)

Token นี้เปรียบเสมือนกุญแจที่ให้ n8n สั่ง LINE ให้ส่งข้อความได้

1. เมื่อสร้าง Channel เสร็จ ระบบจะพาคุณมาที่หน้าจัดการ Channel
2. เลือกแท็บ **"Messaging API"** (ด้านบน)
3. เลื่อนลงมาล่างสุดที่หัวข้อ **Channel access token (long-lived)**
4. คลิกปุ่ม **"Issue"**
5. ระบบจะสร้าง Token ยาวๆ ขึ้นมา (หน้าตาประมาณ `eyJhbGciOiJIUz...`)
6. **สำคัญ:** ก๊อปปี้ Token นี้เก็บไว้ทันที (คุณสามารถกดปุ่ม Reissue เพื่อขอใหม่ได้ตลอดเวลาหากทำหาย)

---

## 🔗 ขั้นตอนที่ 4: ตั้งค่า Webhook URL (ให้ LINE ส่งข้อความมาหา n8n)

เพื่อให้ n8n รู้ว่ามีคนพิมพ์หาบอท คุณต้องตั้งค่า Webhook (คุณต้องมี URL ของ n8n ที่สามารถเข้าถึงจากอินเทอร์เน็ตได้ เช่น ผ่าน Cloudflare Tunnel)

1. เปิด n8n ของคุณขึ้นมา
2. สร้าง Workflow ใหม่
3. ลาก Node **Webhook** มาวาง
4. ดับเบิลคลิกที่ Node Webhook
   - ตั้งค่า **HTTP Method** เป็น `POST`
   - คัดลอก **Test URL** (หรือ **Production URL** หากต้องการใช้จริง) ซึ่งจะหน้าตาคล้ายๆ `https://n8n.your-domain.com/webhook-test/xxxx`
5. กลับมาที่หน้า **LINE Developers Console** (แท็บ Messaging API เดิม)
6. เลื่อนหาหัวข้อ **Webhook URL**
7. คลิก **Edit** และวาง URL ที่ได้จาก n8n ลงไป
8. กด **Update**
9. คลิกปุ่ม **"Verify"** (เพื่อให้ LINE ลองส่งข้อมูลทดสอบไปที่ n8n)
   - *หมายเหตุ: ต้องกดปุ่ม `Listen for Test Event` (หรือปุ่ม Execute) ที่ Node Webhook ใน n8n ก่อนกด Verify เสมอ ไม่งั้นจะขึ้น Error*
10. เปิดสวิตช์ **Use webhook** ให้เป็นสีเขียว (สำคัญมาก!)

---

## 🔌 ขั้นตอนที่ 5: นำ Token ไปใส่ใน n8n

1. กลับมาที่ n8n ของคุณ
2. เพิ่ม Node `LINE` ลงใน Workflow (มักจะต่อจาก Webhook เพื่อใช้ตอบกลับ)
3. ดับเบิลคลิกเปิดการตั้งค่า Node
4. ที่ช่อง **Credential to connect with**
5. เลือก **Create New Credential** (มองหาตัวเลือก LINE API)
6. หน้าต่างตั้งค่าจะให้กรอก:
   - **Credential Name**: เช่น `My LINE OA Key`
   - **Channel Access Token**: วาง Token ยาวๆ ที่ได้จากขั้นตอนที่ 3 ลงไป
7. กดปุ่ม **Save** เพื่อบันทึก

🎉 **เสร็จเรียบร้อย! ตอนนี้ n8n ของคุณสามารถรับ-ส่งข้อความผ่าน LINE ได้อย่างสมบูรณ์แบบ**
