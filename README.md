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

ติดตั้ง n8n บนเครื่องตัวเองพร้อม Cloudflare Tunnel (ให้ได้ **HTTPS** — จำเป็นสำหรับ Webhook และ Chat กับบริการภายนอก):

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

## 🔧 คู่มือการติดตั้ง (Detailed Setup)

### 📋 Prerequisites

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. โดเมนเนมส่วนตัว ([Namecheap](https://www.namecheap.com/) แนะนำ)
3. บัญชี [Cloudflare](https://dash.cloudflare.com/) (ฟรี) — ใช้สร้าง Tunnel เพื่อให้ได้ **HTTPS** (จำเป็นสำหรับ Webhook และ Chat ดูรายละเอียดใน [🔒 ทำไมต้องใช้ HTTPS](#-ทำไมต้องใช้-https-ssl))

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

## 🔒 ทำไมต้องใช้ HTTPS (SSL)

**การไม่มี HTTPS จะทำให้ Webhook และ Chat ใช้งานไม่ได้หรือทำงานไม่ครบ** และมีความเสี่ยงด้านความปลอดภัยดังนี้

### ผลต่อการใช้งาน n8n โดยตรง

| ฟีเจอร์ | ผลเมื่อใช้แค่ HTTP |
|--------|---------------------|
| **Webhook** | ใช้กับ Production **ไม่ได้** — บริการภายนอก (LINE, Telegram, Shopify, GitHub ฯลฯ) กำหนดให้ Webhook URL ต้องเป็น **HTTPS เท่านั้น** จึงจะยอมส่งเหตุการณ์มาได้ |
| **Chat (Chat Trigger / AI Agent)** | ถ้าเข้า n8n ผ่านโดเมนสาธารณะแบบ HTTP ฟีเจอร์ที่พึ่งพา Secure Context ของเบราว์เซอร์ (เช่น บางส่วนของ real-time, Notifications) อาจใช้ไม่ได้ หรือเบราว์เซอร์ขึ้นว่า "Not Secure" |

- n8n ใช้ตัวแปร `WEBHOOK_URL` ต้องเป็น URL เต็มที่ **ขึ้นต้นด้วย `https://`** เพื่อให้ Production Webhook ทำงาน ([n8n docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook), [n8n community](https://community.n8n.io/t/how-to-make-my-webhooks-become-https/20410)).
- แนะนำให้ใช้ Reverse Proxy หรือ Tunnel (เช่น Cloudflare Tunnel) เพื่อให้ได้ HTTPS จริง

### ผลกระทบด้านความปลอดภัยและความน่าเชื่อถือ (จากแหล่งสาธารณะ)

- **ข้อมูลไม่เข้ารหัส (Plaintext)** — ข้อมูลทุกอย่างส่งผ่าน HTTP ถูกส่งแบบไม่เข้ารหัส ทำให้เสี่ยงถูกดักอ่านหรือแก้ไข (Man-in-the-Middle) ([MDN TLS](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/TLS), [MDN MITM](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/MITM)).
- **เบราว์เซอร์และ SEO** — เบราว์เซอร์จะแสดงสถานะ "Not Secure" สำหรับหน้า HTTP และเครื่องมือค้นหาอาจจัดอันดับต่ำลง ([The Web Almanac 2024 - Security](https://almanac.httparchive.org/en/2024/security)).
- **Web APIs ที่ต้องใช้ Secure Context** — APIs ที่เกี่ยวกับความปลอดภัยหรือความเป็นส่วนตัว (เช่น Service Workers, Notifications, Geolocation, Web Crypto, Payment Request) ทำงานได้เฉพาะใน Secure Context (โดยทั่วไปคือ HTTPS หรือ localhost) ([MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts), [Features restricted to secure contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts/features_restricted_to_secure_contexts)).
- **ความเสี่ยงทางธุรกิจและกฎหมาย** — การรั่วไหลข้อมูลจากช่องทางไม่เข้ารหัสอาจนำไปสู่การสูญเสียความเชื่อถือของลูกค้า ค่าปรับตามกฎหมาย (เช่น GDPR) และความเสียหายต่อแบรนด์ ([การวิเคราะห์ความเสี่ยงจากการไม่ใช้ SSL](https://www.oreateai.com/blog/analysis-of-security-risks-and-business-threats-from-not-deploying-ssl-certificates-on-corporate-websites/b7822e9298c6776394216d55c67bf15d)).
- **แนวทาง Webhook จากผู้ให้บริการ** — คู่มือแนวทางปฏิบัติของ GitHub และ Shopify แนะนำให้ส่ง Webhook ผ่าน HTTPS และตรวจสอบลายเซ็น ([GitHub Webhooks Best Practices](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks), [Shopify HTTPS Webhooks](https://shopify.dev/docs/apps/build/webhooks/subscribe/https)).

**สรุป:** สำหรับการใช้งานจริง (โดยเฉพาะ Webhook และ Chat ผ่านโดเมนสาธารณะ) ควรใช้ HTTPS เสมอ โปรเจกต์นี้ใช้ Cloudflare Tunnel เพื่อให้ได้ HTTPS โดยไม่ต้องจัดการ certificate เอง

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
- **ต้องใช้ HTTPS** — Production Webhook ต้องมี URL เป็น `https://` เท่านั้น บริการเช่น LINE, Telegram, Shopify จะไม่ยอมส่งเหตุการณ์มาที่ HTTP
- ตรวจสอบ `WEBHOOK_URL` ใน `.env` ว่าเป็น `https://...` และโดเมนตรงกับที่ Tunnel ชี้
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
