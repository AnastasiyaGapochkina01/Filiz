# Часть 1
1) В директории `/var/www` создать директорию `dvps-03`
2) В директории `dvps-03` создать [файл app.py](https://gist.github.com/AnastasiyaGapochkina01/4c65dba7f26e656b9e6a0d435caa9af4)
3) Запустить приложение командой `python3 app.py`; выяснить
- на каком порту запустилось приложение
- PID процесса, в котором запущено приложение
4) Проверить работу приложения запросами
```
curl 127.0.0.1:$PORT
```
Вывод должен быть похож на
```
anestesia@projects-dev:~$ curl 127.0.0.1:3000
Версия ОС: linux 3.9.2 (default, Mar 20 2025, 02:07:39)
[GCC 10.2.1 20210110]
Приветствие: Привет, anestesia!
Локальный IP: 10.129.0.25
```
5) Убить процесс приложения
# Часть 2
В директории `dvps-03` создать bash-скрипт, который будет
- создавать директорию `/var/www/automate_apps`, если ее еще не существует
- в `/var/www/automate_apps` содавать файл `main.py` с содержимым
```
from flask import Flask
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    python_version = sys.version
    current_directory = os.getcwd()
    return f"Версия Python: {python_version}\nТекущая директория: {current_directory}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
- запускать приложение в фоновом режиме
- проверять, запустилось ли приложение, например проверяя стал ли занят порт 5000
- если все прошло успешно, то выводить собщение `App is started on port $PORT in /var/www/automate_apps`
