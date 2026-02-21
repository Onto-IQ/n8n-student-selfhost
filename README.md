# คู่มือติดตั้ง n8n (Self-Host) สำหรับนักเรียน (ใช้ Cloudflare Tunnels)

ระบบนี้ออกแบบมาสำหรับการเรียนรู้ในชั้นเรียน ช่วยให้นักเรียนสามารถรัน [n8n](https://n8n.io/) บนเครื่อง PC ของตัวเอง (Local) และยังสามารถรับ Webhook จาก API ภายนอก (เช่น LINE, Facebook, Stripe) ผ่านระบบเครือข่ายของมหาวิทยาลัยหรือ Firewall ได้อย่างปลอดภัย โดยใช้ Cloudflare Tunnels

## 📋 สิ่งที่ต้องเตรียม (Prerequisites)

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) ติดตั้งบนเครื่องคอมพิวเตอร์และกำลังทำงานอยู่
2. โดเมนเนมส่วนตัว (สามารถจดราคาประหยัดได้ที่ [Namecheap](https://www.namecheap.com/))
3. บัญชี [Cloudflare](https://dash.cloudflare.com/) (ฟรี)

---

## 🛠️ ขั้นตอนที่ 1: การเตรียม Domain และเชื่อมต่อ Cloudflare

1. **จดโดเมน**: ทำการจดทะเบียน Domain name ที่ต้องการผ่าน Namecheap หรือผู้ให้บริการอื่นๆ
2. **เพิ่ม Site ใน Cloudflare**:
   * สมัครหรือล็อกอินเข้า Cloudflare
   * กด `Add a Site` แล้วใส่ชื่อโดเมนของคุณ
   * เลือกแผนการใช้งานเป็นแบบ `Free`
3. **เปลี่ยน Nameservers**:
   * ไปที่ระบบจัดการโดเมนของ Namecheap (หรือที่ที่คุณจดโดเมนไว้)
   * เปลี่ยน Nameservers ให้เป็นค่าที่ Cloudflare กำหนดมาให้ (มักจะเป็น `xxx.ns.cloudflare.com`)
   * รอให้ระบบอัปเดต (อาจใช้เวลา 5 นาที - 24 ชั่วโมง ขึ้นอยู่กับผู้ให้บริการ)

---

## 🚀 ขั้นตอนที่ 2: สร้าง Zero Trust Tunnel (Cloudflare)

1. ในหน้า Dashboard ของโดเมนคุณที่ Cloudflare ไปที่เมนู **Zero Trust** (อยู่แถบซ้ายมือ)
2. ไปที่ **Networks** -> **Tunnels** แล้วกด `Create a tunnel`
3. เลือก **Cloudflared**
4. ตั้งชื่อ Tunnel ของคุณ (เช่น `n8n-my-pc`) และกด Save
5. ในหน้า **Install and run a connector** ให้ดูในกล่องคำสั่ง Docker 
   * หาคำว่า `--token` แล้วคัดลอก **ข้อความยาวๆ ที่อยู่หลัง --token** เก็บไว้ (นี่คือ `CLOUDFLARE_TUNNEL_TOKEN`)
6. ในหน้า **Route traffic**:
   * **Public hostname**: ใส่ Subdomain (เช่น `n8n`) และเลือก Domain ของคุณ (เช่น `n8n.your-domain.com`)
   * **Service**: เลือก Type เป็น `HTTP` และกำหนด URL เป็น `n8n:5678` (ชี้ไปที่ชื่อ container ของ n8n)
   * กด Save tunnel

---

## 💻 ขั้นตอนที่ 3: ตั้งค่าและรัน n8n บนเครื่องของตนเอง

1. **เตรียมไฟล์ Configuration**:
   คัดลอกไฟล์ `.env.example` แล้วเปลี่ยนชื่อเป็น `.env`
   
   ```bash
   # หากใช้งานบน Windows สามารถก๊อปปี้ผ่าน File Explorer แล้วแก้ชื่อได้เลย
   cp .env.example .env
   ```

2. **แก้ไขไฟล์ `.env`**:
   เปิดไฟล์ `.env` ขึ้นมาด้วย Text Editor (เช่น Notepad, VSCode) และแก้ข้อมูลให้ตรงกับของคุณ:

   ```env
   # เปลี่ยนเป็นรหัสผ่านสำหรับ Database
   POSTGRES_PASSWORD=your_secure_password
   
   # ชื่อโดเมนที่คุณตั้งในขั้นตอนที่ 2.6 (ไม่ต้องใส่ https://)
   N8N_HOST=n8n.your-domain.com
   
   # Webhook URL เต็ม (ต้องมี https://)
   WEBHOOK_URL=https://n8n.your-domain.com/
   
   # Token ที่ก๊อปปี้มาในขั้นตอนที่ 2.5
   CLOUDFLARE_TUNNEL_TOKEN=eyJhIjoi.......
   ```

3. **รัน Docker Compose**:
   เปิด Terminal (หรือ Command Prompt) ในโฟลเดอร์นี้ แล้วพิมพ์คำสั่ง:
   
   ```bash
   docker compose up -d
   ```
   
   *(รอให้ระบบดาวน์โหลด Image และเปิดระบบสักครู่...)*

---

## 🎉 ขั้นตอนที่ 4: เริ่มต้นใช้งาน n8n

1. เปิด Web Browser พิมพ์ `http://localhost:5678` หรือ URL โดเมนของคุณ (เช่น `https://n8n.your-domain.com`)
2. ในการเข้าใช้งานครั้งแรก ระบบจะให้คุณตั้งค่า Owner Account ของ n8n
3. เมื่อเข้าระบบได้แล้ว คุณสามารถสร้าง Workflow และใช้ Webhook URL ส่งออกไปให้ระบบภายนอกเชื่อมต่อเข้ามาได้เลย!

---

## 🛑 การหยุดการทำงาน

เมื่อเลิกใช้งานและต้องการปิด n8n ให้พิมพ์คำสั่งใน Terminal:
```bash
docker compose down
```

> **หมายเหตุ:** โฟลเดอร์ `data` จะถูกสร้างขึ้นมาอัตโนมัติเพื่อเก็บไฟล์ฐานข้อมูลของ n8n และ PostgreSQL ไม่ควรลบโฟลเดอร์นี้หากไม่ต้องการให้ข้อมูลการสร้าง Flow ของคุณหายไป
