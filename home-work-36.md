1) В домашней директории создать директорию linux_again. В ней создать директории lab_01, lab_02 и lab_03
2) В директории lab_01 создать директорию task_01
3) В директории task_01 создать 
- файл readme.md с содержимым
```
# Welcome to Linux
```
- файл data.csv с содержимым
```
"model","year","wheel size","frame material","price"
"Trek Marlin 7","2024","29","Aluminum","95000"
"Specialized Rockhopper","2023","27.5","Aluminum","87000"
"Merida Big Nine 300","2024","29","Aluminum","99000"
"Cube Attention SL","2023","29","Aluminum","105000"
"Scott Scale 970","2024","29","Aluminum","112000"
"Giant Talon 1","2023","27.5","Aluminum","92000"
"Stark Shooter 29.2 D","2024","29","Steel","65000"
"Forward Apache 29 2.0","2023","29","Aluminum","72000"
"Author Solution 29","2024","29","Aluminum","88000"
"Stels Navigator 930 MD","2023","29","Aluminum","69000"
```
4) В файле data.csv найти велосипед со стальной рамой и вывести его модель и стоимость
5) В файле data.csv найти велосипеды, у которых размер колеса (wheel size) составляет 27.5 и вывести их модели, материал рамы и стоимость
6) В директории lab_01 создать директорию task_02
7) В директории task_02 создать
- директорию project-1
- директорию project-2
- файл README.md с содержимым
```
# Project 1: API

# Project 2: Frontend
```
8) Переименовать директорию task_02 в projects
9) Проверить, существует ли пользователь project-admin. Если нет, то создать его
10) Проверить, существует ли пользователь project-qa. Если нет, то создать его
11) Назначить владельцем директории projects пользователя project-admin, а группой владельцев project-qa
12) В директории lab_01 создать директорию archives
13) Скопировать в archives директории task_01 и projects
14) В директории lab_01 создать директорию task_03
15) В директории task_03 создать файлы
- .credentials с содержимым
```
[default]
access_key = xxxx
secret_key = yyyy
```
- config с содержимым
```
address: 192.168.1.1
role: gateway
name: yc-gw-1b
```
16) Назначить права на файл .credentials так, чтобы только владелец мог читать и записывать файл, а группа и все остальные не имели никаких прав на этот файл
17) Назначить права на файл config так, чтобы владелец мог и читать и писать и исполнять файл, группа могла только читать файл, а все остальные не имели никаких прав на этот файл
18) В директории task_01 создать файл nginx_error.log с содержимым
```
2025-04-17T07:45:23 [error] 1234#5678: open() "/var/www/html/missing-page.html" failed (2: No such file or directory), client: 192.168.1.10, server: my-site.com, request: "GET /missing-page.html HTTP/1.1", host: "my-site.com"
2025-04-17T07:46:10 [error] 1234#5678: *15 open() "/var/www/html/forbidden-page.html" failed (13: Permission denied), client: 192.168.1.15, server: my-site.com, request: "GET /forbidden-page.html HTTP/1.1", host: "my-site.com"
2025-04-17T07:47:05 [error] 1234#5678: *23 connect() failed (111: Connection refused) to 127.0.0.1:8080, client: 192.168.1.20, server: my-site.com, request: "GET /api/data HTTP/1.1", host: "my-site.com"
2025-04-17T07:48:00 [error] 1234#5678: *30 SSL_do_handshake() failed (SSL: handshake failure) while SSL handshaking, client: 203.0.113.5, server: my-site.com, request: "GET /secure HTTP/1.1", host: "my-site.com"
2025-04-17T07:48:15 [error] 1234#5678: *35 upstream timed out (110: Connection timed out) while connecting to upstream, client: 192.168.1.25, server: my-site.com, request: "GET /slow-backend HTTP/1.1", upstream: "http://127.0.0.1:9000", host: "my-site.com"
2025-04-17T07:48:20 [error] 1234#5678: *40 no alive upstreams while connecting to upstream, client: 192.168.1.30, server: my-site.com, request: "GET /unavailable HTTP/1.1", upstream: "http://backend", host: "my-site.com"
2025-04-17T07:49:05 [error] 1234#5678: *45 client intended to send too large body: 10485760 bytes, client: 192.168.1.35, server: my-site.com, request: "POST /upload HTTP/1.1", host: "my-site.com"
2025-04-17T07:49:30 [error] 1234#5678: *50 rewrite or internal redirection cycle while processing "/index.html", client: 192.168.1.40, server: my-site.com, request: "GET /index.html HTTP/1.1", host: "my-site.com"
2025-04-17T07:50:12 [error] 1234#5678: *55 invalid number of arguments in "limit_req_zone" directive in /etc/nginx/nginx.conf:45, context: http
2025-04-17T07:50:45 [error] 1234#5678: *60 failed (104: Connection reset by peer) while reading response header from upstream, client: 192.168.1.45, server: my-site.com, request: "GET /api/data HTTP/1.1", upstream: "http://127.0.0.1:8080", host: "my-site.com"
2025-04-17T07:51:10 [error] 1234#5678: *65 unknown directive "fastcgi_passs" in /etc/nginx/sites-enabled/default:12
2025-04-17T07:51:35 [error] 1234#5678: *70 SSL_CTX_use_PrivateKey_file("/etc/ssl/private/server.key") failed (SSL: error:02001002:system library:fopen:No such file or directory:fopen('/etc/ssl/private/server.key','r') error:2006D080:BIO routines:BIO_new_file:no such file), client: 198.51.100.10, server: my-site.com, request: "GET /secure HTTP/1.1", host: "my-site.com"

```
19) В файле nginx_error.log найти строки, содержащие "Connection refused" и вывести для них client_ip
<img width="951" alt="image" src="https://github.com/user-attachments/assets/e98d7d64-8bc5-4c5f-879c-6d7151294dd9" />

20) В файле nginx_error.log найти все ошибки, связанные с SSL
