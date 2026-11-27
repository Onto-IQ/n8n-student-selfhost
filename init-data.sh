#!/bin/bash
# สคริปต์ตั้งค่าฐานข้อมูลครั้งแรก (รันโดย image ของ Postgres ใน container อัตโนมัติ)
# สร้างบัญชี n8n แบบ non-root และให้สิทธิ์เฉพาะฐานข้อมูลที่ใช้งาน
# อ้างอิงจากตัวอย่างทางการ: https://github.com/n8n-io/n8n-hosting
set -e;

if [ -n "${POSTGRES_NON_ROOT_USER:-}" ] && [ -n "${POSTGRES_NON_ROOT_PASSWORD:-}" ]; then
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
		CREATE USER ${POSTGRES_NON_ROOT_USER} WITH PASSWORD '${POSTGRES_NON_ROOT_PASSWORD}';
		GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_NON_ROOT_USER};
		GRANT CREATE ON SCHEMA public TO ${POSTGRES_NON_ROOT_USER};
	EOSQL
else
	echo "SETUP INFO: No Environment variables given!"
fi
