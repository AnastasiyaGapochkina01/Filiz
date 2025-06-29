# Комплексная задача по systemd
## Описание проекта
Проект состоит из 
1) веб-сервера `webapp.py`
	- python-скрипт, запускающий HTTP-сервер на порту 8000.
	- требует доступности базы данных перед стартом - SQLlite
	- логирует ошибки в `/var/log/webapp.log`.
```python
#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import time
import sqlite3

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            try:
                conn = sqlite3.connect('/var/lib/appdb/app.db')
                conn.close()
                self.send_response(200)
            except Exception:
                self.send_response(500)
        else:
            self.send_response(404)

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    server.serve_forever()
```
2) Базы данных `init_db.sh`
	- скрипт инициализации SQLite БД. Создаёт файл БД и таблицу.
	- должен завершиться _перед_ запуском веб-сервера.
```bash
#!/bin/bash
mkdir -p /var/lib/appdb
sqlite3 /var/lib/appdb/app.db "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);"
echo "Database initialized!"
```
## Задачи
1) Создать Unit-файл `app-init-db.service` с типом oneshot, который выполняет инициализацию БД
2) Создать Unit-файл`webapp.service` с типом simple, который запускает `webapp.py`:
- запуск `webapp.service` должен происходить ПОСЛЕ успешного завершения `app-db-init.service`
- `webapp.service` должен автоматически перезапускаться при падении
3) Проверить работоспособность
```bash
curl http://localhost:8000/health
```
