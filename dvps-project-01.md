1) Зайти по ssh на ВМ 
- login
- pass
- ip
2) Установить на ВМ пакеты `python3-pip python3-venv nginx git`
3) В директории `/var/www` создать директорию `dvps-01`
4) В директории `dvps-01` создать файл `app.py` с содержимым
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```
5) Инициализировать в директории `dvps-01` песочиницу `venv` и установить `flask gunicorn`
6) Запустить приложение `app.py` как фоновый процесс
7) Написать bash-скрипт по автоматизации разворачивания приложения
---
Запустить приложение как systemd unit
