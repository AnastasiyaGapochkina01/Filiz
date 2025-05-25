1) В домашней директории выполнить команду
```
git clone https://gist.github.com/1ea1e2dae7f6dcb2f80a94954bfc6352.git
```
3) Проверить, появилась ли в домашней директории директория 1ea1e2dae7f6dcb2f80a94954bfc6352; если да, то переименовать ее в `linux`; если нет - создать директорию `linux` и в ней создать файл `create_app.sh`
с содержимым, взятым по ссылке https://gist.github.com/AnastasiyaGapochkina01/1ea1e2dae7f6dcb2f80a94954bfc6352
4) Перейти в директорию linux, сделать файл `create_app.sh` исполняемым и выполнить `./create_app.sh`
5) Проверить, появилась ли в директории linux директория с именем, похожим на `linux-project_1748142597`, если да, то вывести с помощью `tree` ее дерево; должно получиться примерно так
```
linux-project_1748142597
├── docs
│   └── readme.md
├── logs
│   ├── app-access.log
│   └── app.log
└── src
    ├── app.cfg
    └── app.php
```
6) В директории linux создать директорию `linux_projects_bkp`
7) Скопировать всю директорию `linux-project_1748142597` в `linux_projects_bkp`
8) В файле `logs/app-access.log` найти все строки, содержащие `welcome`
9) В файле `logs/app-access.log` найти все запросы, которые шли на `/app_dev.php`
10) В файле `src/app.cfg` найти данные для подключения к БД (username и password)
11) Переименовать файл `scr/app.php` в `logs.php`
12) В файле `logs/app.log` найти записи, относящиеся к Payment и вывести для них **значение** transaction_id
13) В файле `logs/app.log` найти все записи Warning и вывести для них только дату и сообщение
<img width="764" alt="image" src="https://github.com/user-attachments/assets/5637cf91-5f0c-4b19-b139-94259827d562" />

14) Создать пользователя linux-admin и группу linux-apps
15) Назначить права на директорию `linux-project_1748142597` так, чтобы владельцем был linux-admin, а группой владельцев linux-apps
16) Назначить права на директорию `linux-project_1748142597` так, чтобы владелец и группа имели полные права, а все остальные могли только просматривать содержимое директории
17) Создать пользователя linux-user, добавить его в группу linux-apps; проверить, может ли linux-user выполнять действия в директории `linux-project_1748142597`
18) В директории `linux` создать файл `workers.py` с содержимым
```
#!/usr/bin/python3
import subprocess

def start_worker_processes():
    log_file = "workers.log"
    with open(log_file, "a") as log:
        proc1 = subprocess.Popen(['sleep', '60000'])
        log.write(f"Started process 1 with PID {proc1.pid} named 'worker-linux-app'\n")

        proc2 = subprocess.Popen(['sleep', '60000'])
        log.write(f"Started process 2 with PID {proc2.pid} named 'worker-linux-app'\n")

if __name__ == "__main__":
    start_worker_processes()
```
19) Сделать файл `workers.py` исполняемым и запустить `./workers.py`
20) Что делает этот скрипт?
21) Найти дочерние процессы, которые запустил этот скрипт; посчитать их количество
22) Убить дочерние процессы, которые запустил этот скрипт
23) Запустить еще раз `workers.py` и найти PPID его дочерних процессов
24) Убить дочерние процессы, которые запустил `workers.py`
