# Часть 1
1) В директории text_processing создать файл mixed_logs с содержимым
```
2025-01-26 09:15:23 [Web-Server] [INFO] HTTP request was received from 192.168.1.100
2025-01-26 09:15:24 [Database] [ERROR] Database connection error
2025-01-26 09:15:25 [Authentication] [WARN] Exceeded the number of failed login attempts
2025-01-26 09:15:26 [Payment-Gateway] [INFO] Exceeded the number of failed login attempts
2025-01-26 09:15:27 [Email-Service] [DEBUG] Sending a message to a user user@example.com
2025-01-26 09:15:23 [Web-Server] [INFO] HTTP request was received from 192.168.1.4
2025-01-26 09:15:28 [Security] [CRITICAL] Suspicious activity detected
2025-01-26 09:22:55 [Web-Server] [DEBUG] Sending a message to a user user@example.com
2025-01-26 09:22:55 [Database] [ERROR] СHTTP request was received from 192.168.1.4
2025-01-26 09:22:55 [Database] [WARN] HTTP request was received from 192.168.1.6
```
2) С помощью grep и регулярных выражений из файла mixed_logs получить
- ip-адреса
- названия сервисов
- email
- время
3) В директории text_processing выполнить команду
```
wget https://raw.githubusercontent.com/AnastasiyaGapochkina01/Filiz/refs/heads/main/inventory.ini
```
4) Проверить, появился ли файл в директории text_processing inventory.ini. Если да, то вывести из него первые 15 строк, а после вывести из этого файла строки с 10 по 16.
5) С помощью grep и регулярных выражений из файла inventory.ini получить значения item_id
6) В директории text_processing создать файл user_data с содержимым
```
apple developer [code: 201] projects: [afina, logger]
cherry admin [code: 100] projects: [all]
fox developer [code: 202] projects: [afina]
kris manager [code: 303] projects: [logger, disco]
kira developer [code: 200] projects: [afina, logger, disco]
```
7) С помощью grep и регулярных выражений из файла user_data получить
- code
- projects
8) В директории text_processing создать файл colors с содержимым
```
White	#FFFFFF	255,255,255
Black	0,0,0 #000000
Red	#FF0000	255,0,0
Green	#00FF00	0,255,0
Blue	#0000FF	0,0,255
```
9) С помощью grep и регулярных выражений из файла colors получить коды цветов в шестнадцатеричном формате

<img width="373" alt="image" src="https://github.com/user-attachments/assets/6adfd04b-d640-4668-a425-f65652ad7182" />

10) В директории text_processing создать файл books с содержимым
```
M.Y. Lermontov A hero of our time ISBN: 978-5-901202-50-0
ISBN: 978-5-699-12014-7 War and Peace L.N. Tolstoy
Crime and punishment F.M. Dostoevsky ISBN: 978-5-389-01556-2
M.A. Bulgakov ISBN: 978-5-17-078799-4 The Master and Margarita 
```
11) С помощью grep и регулярных выражений из файла books получить все ISBN
12) С помощью grep и регулярных выражений из файла books получить всех авторов
13) В директории text_processing создать файл list_of_all_files с содержимым
```
index.html - https://main.com
index.css
view.html - http://look-main.com
process_form.php
ajax.js
deploy.sh
cron.php
login.js
```
14) С помощью grep и регулярных выражений из файла list_of_all_files получить url

<img width="310" alt="image" src="https://github.com/user-attachments/assets/b7ccf937-853f-47fc-9d50-be52c2c11e4b" />

# Часть 2
1) В директории text_processing/process создать файл log_ping.sh с содержимым
```
#!/bin/bash

mkdir -p ./ping_logs

while true; do
    current_datetime=$(date "+%Y-%m-%d %H:%M:%S")

    ping_result=$(ping -c 1 google.com)

    if echo "$ping_result" | grep -q "0% packet loss"; then
        status="Success"
    else
        status="Failed"
    fi

    response_time=$(echo "$ping_result" | grep "time=" | cut -d "=" -f 4)

    echo "$current_datetime ping from $(hostname) $status $response_time" >> ./ping_logs/ping_log_$(date "+%Y-%m-%d").txt

    sleep 60
done
```
2) Сделать файл log_ping.sh исполняемым
3) Выполнить команду ```./log_ping.sh &```
4) Проверить, появилась ли в директории process директория ping_logs, если да -- проверить есть ли в ней файл с именем которое содержит в себе ```ping_log```, если да, то вывести из него первые 2 строки
5) Найти с помощью ps процесс log_ping и вывести для него ppid,pid,stat,comm
6) Приостановить процесс log_ping; проверить как изменился столбец stat
7) Возобновить процесс log_ping; проверить как изменился столбец stat
8) Убить процесс log_ping
9) В директории text_processing/process выполнить ```for i in {1..3}; do ./log_ping.sh & done```
10) Посчитать количество процессов log_ping с помощью ps и wc
11) Найти id процессов log_ping
12) Найти в директории /proc все директории, которые соответствуют найденным id процессов
13) Убить все процессы log_ping
