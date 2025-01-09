# Часть 1
1) В домашней директории создать директорию pings
2) В директории pings создать файл run.sh с содержимым
```
#!/bin/bash

ping -c 10000 google.com > ping_google.log &

ping -c 10000 yandex.ru > ping_yandex.log &

echo "$(date +'%Y-%m-%dT%H:%M:%S') Processes ping running in the background" >> pings.out

wait

echo "$(date +'%Y-%m-%dT%H:%M:%S') All ping processes are completed" >> pings.out
```
3) Сделать файл run.sh исполняемым для всех
4) Выполнить команду ```./pings.sh > /dev/null &```
5) Найти все процессы ping с помощью ps
6) Вывести ppid, pid и command для найденных процессов ping
7) Найти в директории /proc директории, которые соответствуют найденным процессам ping
8) Проверить, появился ли в директории pings файл pings.out, если да, то посмотреть его содержимое
9) Убить все процессы ping
10) Еще раз выполнить команду ```./pings.sh > /dev/null &```
11) Найти процесс run.sh в выводе ps
12) Выполнить ```ps -f -o stat -g <PID процесса run.sh>```
13) Отправить сигнал STOP процессу run.sh
14) Проверить изменился ли его статус ```ps -f -o stat -g <PID процесса run.sh>```
15) Отправить сигнал CONT процессу run.sh и проверить изменился ли его статус
# Часть 2
1) В домашней директории создать директорию temp-files
2) В temp-files создать файлы test.txt main.go server.py и директорию copies
3) Скопировать файлы test.txt main.go server.py в директорию copies
4) Переименовать файл copies/test.txt в tests.py
5) Создать директорию python и скопировать в нее файлы server.py и tests.py
6) Создать директорию go и переместить в нее файл main.go
7) Из директории temp-files удалить все файлы.
Директории copies, python и go должны остаться вместе с содержимым, те при выполнении ls и tree в директории temp-files выывод должен быть такой:
```
~/temp-files » ls
copies go     python

~/temp-files » tree -a
.
├── copies
│   ├── main.go
│   ├── server.py
│   └── tests.py
├── go
│   └── main.go
└── python
    ├── server.py
    └── tests.py

4 directories, 6 files
```
8) В домашней директории создать директорию temp-backups
9) Скопировать все содержимое директории temp-files в temp-backups
10) В директории temp-backups создать файл bkp-credentials
11) Переименовать файл bkp-credentials в .env
12) Удалить директорию temp-files
# Часть 3
1) Проверить, существует ли файл /etc/ssh/sshd_config, если да, то вывести его без строк, начинающихся с #
2) Из файла /etc/passwd вывести только имена всех пользователей
3) С помощью grep получить модель процессора из файла /proc/cpuinfo
4) Проверить, существует ли файл /etc/X11/Xsession.options, если да, то вывести из него все строки, начинающиеся с allow
5) Из файла /etc/lsb-release получить значение DISTRIB_CODENAME
6) Проверить, существует ли файл /etc/netconfig, если да, то вывести его без строк, начинающихся с #, а затем получить первый столбец
7) Проверить, существует ли файл /etc/xattr.conf, если да, то вывести его без строк, начинающихся с #, а затем исключить из вывода строки, содержащие skip
8) Проверить, существует ли файл /etc/protocols, если да, то найти в нем tcp и upd (сделать одним грепом)
9) Выполнить команду lsblk. Если в ее выводе есть loop - исключить их. Затем получить столбец SIZE для строки, в которой содержится слово disk
10) Из вывода команды ip -4 -o a получить только первую строчку
