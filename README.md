# 🎓 n8n Student Self-Host - คู่มือสำหรับนักเรียน

โปรเจกต์นี้รวมทั้ง **ระบบติดตั้ง n8n แบบ Self-Host** และ **ชุด Workflow สำหรับการเรียนการสอน** ตั้งแต่พื้นฐานจนถึงระดับสูง

## 📂 โครงสร้างโปรเจกต์

```
n8n-student-selfhost/
├── 📁 workflows/              # ชุด Workflow สำหรับการเรียน
│   ├── 01_Basics/            # พื้นฐาน n8n (6 workflows)
│   ├── 02_AI_Agents_Basics/  # AI Agents (5 workflows)
│   └── 03_Used_Cases/        # Use Cases จริง (7 workflows)
│
├── 📁 Credentials/           # คู่มือการตั้งค่า Credentials
│   ├── google-oauth.md
│   ├── line-api.md
│   └── openai-api.md
│
├── 📁 Case Studies/          # ตัวอย่าง Case จากธุรกิจจริง
├── docker-compose.yml        # ไฟล์สำหรับรัน n8n
├── .env.example             # ตัวอย่างการตั้งค่า
└── README.md                # ไฟล์นี้
```

---

## 🚀 Quick Start - เริ่มต้นใช้งาน

### สำหรับผู้ที่ยังไม่มี n8n

ติดตั้ง n8n บนเครื่องตัวเองพร้อม Cloudflare Tunnel (สำหรับรับ Webhook):

1. **Clone โปรเจกต์**
   ```bash
   git clone https://github.com/Onto-IQ/n8n-student-selfhost.git
   cd n8n-student-selfhost
   ```

2. **ตั้งค่า Environment**
   ```bash
   cp .env.example .env
   # แก้ไขไฟล์ .env ตามคู่มือด้านล่าง
   ```

3. **รัน n8n**
   ```bash
   docker compose up -d
   ```

4. **เข้าใช้งาน**
   - Local: http://localhost:5678
   - Online: https://n8n.your-domain.com (ถ้าตั้งค่า Cloudflare Tunnel)

---

## 📚 เนื้อหาการเรียน (18 Workflows)

### 🌱 Phase 1: พื้นฐาน (01_Basics)
สำหรับผู้ไม่เคยใช้ n8n - [ดูรายละเอียด](workflows/01_Basics/README.md)

| ลำดับ | หัวข้อ | สิ่งที่เรียนรู้ |
|-------|--------|----------------|
| 01 | JSON Basics | Key-Value, Data Types |
| 02 | Flow Control | IF, Switch Nodes |
| 03 | Loop | Loop, Item Lists |
| 04 | Data Transformation | Edit Fields, Code Node |
| 05 | External APIs | HTTP Request |
| 06 | Webhooks | Webhook Trigger |

**⏱️ เวลา:** 1-2 วัน

---

### 🚀 Phase 2: AI Agents (02_AI_Agents_Basics)
เริ่มสร้าง AI Agents - [ดูรายละเอียด](workflows/02_AI_Agents_Basics/README.md)

| ลำดับ | หัวข้อ | สิ่งที่เรียนรู้ |
|-------|--------|----------------|
| 01 | Basic Chat Agent | AI Agent + Memory |
| 02 | Agent with Tools | Function Calling |
| 03 | Simple RAG | AI อ่านเอกสาร |
| 04 | MCP Client | เชื่อม External Tools |
| 04 | MCP Server | เปิด n8n เป็น Server |

**⏱️ เวลา:** 2-3 วัน

---

### 🎯 Phase 3: Use Cases จริง (03_Used_Cases)
ตัวอย่างจากโลกธุรกิจ - [ดูรายละเอียด](workflows/03_Used_Cases/README.md)

| ระดับ | ไฟล์ | ใช้งาน |
|-------|------|--------|
| 🟢 พื้นฐาน | LINE Chat Gemini | Chat Bot |
| 🟢 พื้นฐาน | Form → Google Workspace | ระบบรับเรื่อง |
| 🟡 กลาง | Candidate Screening | HR Automation |
| 🟡 กลาง | RAG with Pinecone | Vector DB |
| 🔴 สูง | Multi-Agent Linear | Sequential Pattern |
| 🔴 สูง | Multi-Agent Orchestration | 2026 Pattern |
| 🔴 สูง | Sub-Workflows | Modular Design |

**⏱️ เวลา:** 3-5 วัน

---

## �️ คู่มือการติดตั้ง (Detailed Setup)

### 📋 Prerequisites

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. โดเมนเนมส่วนตัว ([Namecheap](https://www.namecheap.com/) แนะนำ)
3. บัญชี [Cloudflare](https://dash.cloudflare.com/) (ฟรี)

### ขั้นตอนที่ 1: เตรียม Domain และ Cloudflare

1. **จดโดเมน** ที่ Namecheap หรือผู้ให้บริการอื่น
2. **เพิ่ม Site ใน Cloudflare**:
   - เข้า Cloudflare → Add a Site → ใส่โดเมน
   - เลือก Free Plan
3. **เปลี่ยน Nameservers** ที่ Namecheap เป็นค่าที่ Cloudflare ให้มา
   - รอ 5 นาที - 24 ชั่วโมง

### ขั้นตอนที่ 2: สร้าง Cloudflare Tunnel

1. Cloudflare Dashboard → **Zero Trust** → **Networks** → **Tunnels**
2. **Create a tunnel** → เลือก **Cloudflared**
3. ตั้งชื่อ Tunnel (เช่น `n8n-my-pc`)
4. คัดลอก **Token** จากคำสั่ง Docker (หลัง `--token`)
5. **Route traffic**:
   - Public hostname: `n8n.your-domain.com`
   - Service: HTTP → `n8n:5678`

### ขั้นตอนที่ 3: ตั้งค่า .env และรัน

```bash
# 1. คัดลอกไฟล์ตั้งค่า
cp .env.example .env

# 2. แก้ไข .env ด้วย Text Editor
# POSTGRES_PASSWORD=your_password
# N8N_HOST=n8n.your-domain.com
# WEBHOOK_URL=https://n8n.your-domain.com/
# CLOUDFLARE_TUNNEL_TOKEN=eyJh...

# 3. รัน n8n
docker compose up -d
```

### ขั้นตอนที่ 4: เข้าใช้งาน

- Local: http://localhost:5678
- Online: https://n8n.your-domain.com
- ตั้งค่า Owner Account ครั้งแรก

---

## 🛑 การจัดการ n8n

### หยุดการทำงาน
```bash
docker compose down
```

### ดู Logs
```bash
docker compose logs -f n8n
```

### อัปเดต n8n เป็นเวอร์ชันล่าสุด
```bash
docker compose pull
docker compose up -d
```

### สำรองข้อมูล (Backup)
โฟลเดอร์ `data/` เก็บข้อมูลทั้งหมดของ n8n ควรสำรองก่อนลบ Container:

| โฟลเดอร์ | เก็บอะไร |
|----------|----------|
| `data/postgres/` | ฐานข้อมูล (workflows, credentials ที่เข้ารหัสแล้ว, execution) |
| `data/n8n/` | Config และ **Encryption Key** ที่ n8n ใช้ถอดรหัส credentials ใน DB |

```bash
# สำรองทั้งคู่ (ต้องมีทั้งสองถึงจะ restore ได้ครบ)
cp -r data data-backup-$(date +%Y%m%d)
```

> **⚠️ คำเตือน:** อย่าลบโฟลเดอร์ `data/` ถ้าต้องการเก็บ Workflow และ Credentials ที่สร้างไว้

### กู้คืนข้อมูล (Restore)
เพื่อให้ใช้ได้ทันทีหลัง restore:
1. นำโฟลเดอร์ที่ backup กลับมาเป็น `data/` (หรือ copy เนื้อหาใน `data-backup-xxx/postgres` และ `data-backup-xxx/n8n` ไปที่ `data/postgres` และ `data/n8n`)
2. ใช้ค่า `.env` เดิม (อย่างน้อย `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`) ให้ตรงกับตอน backup
3. รัน `docker compose up -d` — workflows และ credentials จะใช้ได้ตามเดิม

ถ้าไม่มี `data/n8n` (หรือ Encryption Key ไม่ตรงกับตอน backup) credentials ใน DB จะถอดรหัสไม่ได้

---

## 🆘 แก้ไขปัญหาเบื้องต้น

### n8n ไม่เปิด
```bash
# ตรวจสอบสถานะ
docker compose ps

# ดู error
docker compose logs n8n
```

### Webhook ไม่ทำงาน
- ตรวจสอบ `WEBHOOK_URL` ใน `.env`
- ตรวจสอบ Cloudflare Tunnel ทำงานอยู่หรือไม่
- ทดสอบ: `curl https://n8n.your-domain.com/webhook-test`

### ลืมรหัสผ่าน n8n
```bash
# Reset owner account
docker compose exec n8n n8n user-management:reset
```

---

## 📖 เอกสารอื่นๆ

- [📁 คู่มือ Credentials](Credentials/) - วิธีขอ API Key ต่างๆ
- [📁 ตัวอย่าง Case Studies](Case%20Studies/) - จากธุรกิจจริง
- [🌐 n8n Documentation](https://docs.n8n.io/)
- [💬 n8n Community](https://community.n8n.io/)

---

## 📝 License

MIT License - ใช้เพื่อการศึกษาได้ฟรี

---

<div align="center">

**สร้างด้วย ❤️ สำหรับนักเรียน n8n**

[เริ่มเรียน Phase 1 →](workflows/01_Basics/README.md)

</div>
