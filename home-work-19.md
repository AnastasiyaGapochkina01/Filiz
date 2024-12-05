# Часть 1: Пользователи и права доступа
1) Создать пользователей master и slave
2) Создать группу main
3) Добавить пользователя master в группы sudo и main
4) Назначить пользователю master пароль
5) В директории /opt создать директорию database
6) В директории database создать директории main и third
7) Назначить владельцем директории main пользователя master
8) Назначить владельцем директории third пользователя slave
9) Переключиться на пользователя master и перейти в директорию /opt/main. Если перейти получилось, то в этой директории создать
- файлы my.cnf, limits, .env
- директорию data
10) Выйти из под пользователя master
11) Переключиться на пользователя slave и перейти в директорию /opt/third. Если перейти получилось, то в этой директории создать
- файлы wal1, wal2
12) Выйти из под пользователя slave
13) Назначить группой владельцев директорий database, main и third группу main
14) Установить права на директории database, main и third так чтобы владелец и группа имели полные права, а все остальные никаких
15) Создать пользователя alice с домашней директорией /home/alice_in_wonderland
16) Переключиться на пользователя alice
- попробовать перейти в /opt/database/main. Если получилось - попробовать создать там файл с именем emptyfile
- попробовать перейти в /opt/database/third. Если получилось - попробовать создать там файл с именем emptyfile
- выйти из под пользователя alice
18) Посмотреть права на созданные директории
```
ls -lA /opt/database/
ls -lA /opt/database/main
ls -lA /opt/database/third
```
19) В директории /opt/database создать директорию pub_uploads
20) Назначить права на директорию pub_uploads так чтобы владелец мог только исполнять, группа могла читать и исполнять, а все остальные не имели никаких прав
21) Назначить владельцем директории pub_uploads пользователя nobody, а группой владельцев - main
# Часть 2: Работа с процессами
1) В домашней директории создать файл alt_top с содержимым
```
#!/bin/bash

LOG_FILE="server.log"

while true; do
    top_processes=$(ps -eo pid,comm,%cpu --sort=-%cpu | head -n 3 | tail -n 2)

    echo "$(date): Top CPU consuming processes:" >> $LOG_FILE
    echo "$top_processes" >> $LOG_FILE
    echo "----------------------------------------" >> $LOG_FILE

    sleep 5
done
```
2) Сделать файл alt_top исполняемым для всех
3) Выполнить команду ```./alt_top &> /dev/null &```
4) Найти id процесса alt_top
5) Посмотреть список файлов в домашней директории. Какой файл добавился? Какой в нем текст?
6) В директории /proc найти каталог, который соответствует найденному выше id процесса alt_top
7) Убить процесс alt_top
# Часть 3: Работа с текстом
1) В директории text_processing создать файл nginx-demo.log с содержимым
```
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:03:51 +0300] "GET /my_author.php HTTP/1.0" 302 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.057)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:03:51 +0300] "GET /auth.php?ref=my_author.php HTTP/1.0" 302 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.033)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:03:51 +0300] "GET /my_author.php HTTP/1.0" 302 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.058)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:03:53 +0300] "GET /password.php HTTP/1.0" 200 14496 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:2.124)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:04:23 +0300] "GET / HTTP/1.0" 404 307 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.001)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:04:33 +0300] "GET /password.php HTTP/1.0" 404 319 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.000)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:04:53 +0300] "GET /password.php HTTP/1.0" 404 319 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.001)
10.144.83.128 173.205.85.42, 173.205.85.42 - - [02/Dec/2024:15:06:22 +0300] "GET / HTTP/1.0" 404 307 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" (time:0.000)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:06:54 +0300] "GET /password.php HTTP/1.0" 404 319 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.001)
10.144.83.128 130.193.52.238, 130.193.52.238 - - [02/Dec/2024:15:07:13 +0300] "GET /password.php HTTP/1.0" 404 319 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" (time:0.000)
```
2) В файле nginx-demo.log найти все запросы, содержащие my_author
3) В файле nginx-demo.log найти все строки, содержащие 404 и вывести для них все ip-адреса
4) Из файла /etc/passwd получить имена и id пользователей
5) В файле /etc/passwd пользователей найти master и slave
6) Из файла /etc/passwd вывести значение домашней директории пользователя alice
7) Проверить существует ли файл K01udev в директории /etc/rc0.d, если существует, то найти в нем значение PIDFILE и проверить существует ли этот файл
8) Проверить, существует ли файл /etc/selinux/semanage.conf, если существует, то вывести его на экран без строк, начинающихся с символа #
9) Из файла /proc/zoneinfo получить значения pages free
10) Из вывода команды printenv получить значение переменной USER
11) В директории text_processing создать файл  emtyfile
12) Из вывода команды ```stat emtyfile``` получить Uid и Gid
