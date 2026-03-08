1) Написать роль, которая
- установит Prometheus (НЕ в Docker)
- настроит основной конфиг `/etc/prometheus/prometheus.yml` из шаблона с переменными: `scrape_interval: "{{ scrape_interval }}"`
- добавит пользователя `prometheus` без shell, с домашней директорией `/var/lib/prometheus`
2) Написать роль, которая:
- установит Grafana (из репозитория или пакета, НЕ в Docker).
- настроит `grafana.ini` из шаблона: 
```
admin_user: "{{ grafana_admin }}"
admin_password: "{{ grafana_pass }}"
server.http_port: "{{ grafana_port | default(3000) }}"
```
3) Написать роль, которая:
- становит rsync, создаст пользователя `backup`
- создаст `/etc/rsync-backup.conf` из шаблона:
```
path /data
target_host "{{ backup_server }}:/backups/"
```
- добавит cron: `0 2 * * * /usr/local/bin/backup.sh`
- скопирует скрипт `backup.sh` в `/usr/local/bin/backup.sh`

файл backup.sh
```bash
#!/bin/bash

BACKUP_ROOT="/backup"
SOURCE_DIRS="/etc /var/www"
LOG_FILE="/var/log/backup.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

if [[ $EUID -ne 0 ]]; then
    log "ERROR: Скрипт должен запускаться от root"
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$BACKUP_ROOT/$(hostname)/current"

mkdir -p "$BACKUP_DIR"
log "Запуск бэкапа: $SOURCE_DIRS -> $BACKUP_DIR"
```
