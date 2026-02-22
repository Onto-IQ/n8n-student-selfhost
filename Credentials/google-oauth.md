# 📧 คู่มือการเชื่อมต่อ Google Workspace (OAuth2)

การเชื่อมต่อ Google (เช่น Gmail, Google Sheets, Google Drive) จะใช้ระบบ OAuth2 ซึ่งมีความปลอดภัยสูง เพราะไม่ต้องใช้รหัสผ่าน (Password) ของอีเมลโดยตรง แต่จะเป็นการ "อนุญาต (Authorize)" ให้ n8n เข้าถึงข้อมูลแทน

> **หมายเหตุ:** สำหรับ n8n แบบ Self-hosted คุณจำเป็นต้องสร้าง Credentials เป็นแบบ **Web application** หรือ **Desktop app** (แนะนำให้ใช้ Web application และระบุ Redirect URI)

---

## 🛠️ ขั้นตอนที่ 1: สร้าง Project ใน Google Cloud Console

1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. ล็อกอินด้วยบัญชี Google ของคุณ (แนะนำให้ใช้บัญชีเดียวกับที่จะใช้ในแบบฝึกหัด)
3. ที่แถบเมนูด้านบน (ข้างๆ โลโก้ Google Cloud) คลิกเลือก Project
4. หน้าต่างย่อยจะเปิดขึ้นมา ให้คลิก **"New Project"** (มุมขวาบน)
5. ตั้งชื่อโปรเจกต์ เช่น `n8n-student-course` แล้วกด **Create**
6. รอระบบสร้างสักครู่ แล้วเลือกโปรเจกต์ที่คุณเพิ่งสร้าง

---

## 🛡️ ขั้นตอนที่ 2: ตั้งค่า OAuth Consent Screen

*นี่คือหน้าจอที่จะโผล่มาถามว่า "คุณอนุญาตให้แอปนี้เข้าถึงข้อมูลไหม?"*

1. ที่เมนูด้านซ้าย เลือก **"APIs & Services"** > **"OAuth consent screen"**
2. ในส่วน User Type ให้เลือก **"External"** (หรือ Internal ถ้าคุณใช้ Google Workspace ขององค์กร) แล้วกด **Create**
3. กรอกข้อมูล **App information**:
   - **App name**: `n8n Student App` (หรือชื่ออะไรก็ได้)
   - **User support email**: ใส่อีเมลของคุณ
4. เลื่อนลงมาล่างสุดที่ **Developer contact information**:
   - ใส่อีเมลของคุณอีกครั้ง
5. กด **Save and Continue** 
6. หน้า Scopes ข้ามไปก่อนได้ กด **Save and Continue**
7. หน้า Test users สำคัญมาก! คลิก **"ADD USERS"** และใส่อีเมลของคุณ (อีเมลที่จะใช้ทดสอบ) กด **Add** และ **Save and Continue**
8. (สำคัญ) ในหน้าสรุป กลับไปที่ Dashboard ของ OAuth consent screen คลิกปุ่ม **"PUBLISH APP"** และกดยืนยัน (Confirm) เพื่อเปลี่ยนสถานะเป็น In production (จะได้ไม่ต้องกังวลเรื่อง Token หมดอายุใน 7 วัน)

---

## 🔌 ขั้นตอนที่ 3: เปิดใช้งาน APIs (Enable APIs)

คุณต้องบอก Google ว่าคุณจะใช้บริการอะไรบ้าง

1. ที่เมนูด้านซ้าย เลือก **"APIs & Services"** > **"Library"**
2. ค้นหาและเปิดใช้งาน (Enable) APIs ที่คุณต้องการใช้ในแบบฝึกหัด:
   - ค้นหา `Gmail API` > กด **Enable**
   - ค้นหา `Google Sheets API` > กด **Enable**
   - ค้นหา `Google Drive API` > กด **Enable**

---

## 🔑 ขั้นตอนที่ 4: สร้าง OAuth Credentials (Client ID & Secret)

1. ที่เมนูด้านซ้าย เลือก **"APIs & Services"** > **"Credentials"**
2. คลิกปุ่ม **"+ CREATE CREDENTIALS"** (ด้านบน) และเลือก **"OAuth client ID"**
3. เลือก **Application type** เป็น **"Web application"**
4. ตั้งชื่อ (Name) เช่น `n8n Web Client`
5. ในส่วน **Authorized redirect URIs**:
   - คุณต้องเอา URL จากระบบ n8n มาใส่
   - เปิด n8n ของคุณขึ้นมา
   - ลาก Node เช่น `Google Sheets` มาวาง > ดับเบิลคลิกเปิดตั้งค่า
   - ส่วน Credential เลือก `Create New Credential`
   - เลือก **Google Sheets OAuth2 API**
   - ในหน้าต่าง Credential ของ n8n จะมีกล่องข้อความ **OAuth Redirect URL** (เช่น `https://n8n.your-domain.com/rest/oauth2-credential/callback`)
   - ก๊อปปี้ URL นั้น มาใส่ในช่อง Authorized redirect URIs ใน Google Cloud Console กด **ADD URI**
6. กด **Create**
7. Google จะแสดงหน้าต่างที่มี **Client ID** และ **Client Secret**

---

## 🔗 ขั้นตอนที่ 5: นำไปใส่ใน n8n

1. กลับมาที่หน้าต่าง Credential ของ n8n
2. นำ **Client ID** และ **Client Secret** ที่ได้จากหน้าต่าง Google มาใส่
3. กดปุ่ม **"Sign in with Google"**
4. จะมีหน้าต่างป๊อปอัปให้เลือกล็อกอินบัญชี Google (เลือกบัญชีเดียวกับที่คุณแอดใน Test users)
5. กดยอมรับ (Allow) ทุกเงื่อนไข
6. ถ้าสำเร็จ n8n จะขึ้นข้อความ **"Account connected"** สีเขียว
7. กด **Save** และปิดหน้าต่าง Credential

🎉 **เสร็จเรียบร้อย! ตอนนี้คุณสามารถใช้ Node Gmail, Google Sheets, Drive ได้แล้ว**
