# Часть 1: Работа с текстом
1) В директории text_processing создать файл mysql.log с содержимым
```
2024-11-06T08:00:01.123456Z 0 [Note] /usr/sbin/mysqld: ready for connections.
2024-11-06T08:00:05.234567Z 2 [Warning] Access denied for user 'root'@'localhost' (using password: NO)
2024-11-06T08:00:10.345678Z 3 [Note] /usr/sbin/mysqld: Normal shutdown
2024-11-06T08:00:15.456789Z 0 [Note] InnoDB: Starting shutdown...
2024-11-06T08:00:20.567890Z 0 [Note] InnoDB: Shutdown completed; log sequence number 1234567
2024-11-06T08:00:25.678901Z 0 [Note] /usr/sbin/mysqld: Shutdown complete

2024-11-06T08:01:00.789012Z 0 [Note] /usr/sbin/mysqld: ready for connections.
2024-11-06T08:01:05.890123Z 4 [Note] Access denied for user 'admin'@'192.168.1.100' (using password: YES)
2024-11-06T08:01:10.901234Z 5 [Warning] Aborted connection 5 to db: 'mydb' user: 'user1' host: 'localhost' (Got an error reading communication packets)
2024-11-06T08:01:15.012345Z 6 [Note] Created TEMPORARY table for derived table
2024-11-06T08:01:20.123456Z 7 [Warning] Unsafe statement written to the binary log using statement format since BINLOG_FORMAT = STATEMENT.
```
2) В файле mysql.log найти все записи содержащие "_Access denied_" и вывести для них адреса, с которых был запрос
3) Вывести из файла mysql.log записи содержащие "_Warning_"
4) В директории text_processing создать файл nginx.log с содержимым
```
192.168.1.100 - - [06/Nov/2024:08:30:15 +0300] "GET /index.html HTTP/1.1" 200 1234 "http://example.com" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
203.0.113.5 - - [06/Nov/2024:08:30:16 +0300] "POST /api/login HTTP/1.1" 401 173 "-" "PostmanRuntime/7.29.2"
10.0.0.1 - - [06/Nov/2024:08:30:17 +0300] "GET /images/logo.png HTTP/1.1" 304 0 "http://example.com/about" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
192.168.1.101 - - [06/Nov/2024:08:30:18 +0300] "GET /css/style.css HTTP/1.1" 200 4321 "http://example.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1"
203.0.113.10 - - [06/Nov/2024:08:30:19 +0300] "GET /api/users HTTP/1.1" 403 234 "-" "curl/7.68.0"
192.168.1.102 - - [06/Nov/2024:08:30:20 +0300] "GET /blog HTTP/1.1" 301 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
10.0.0.2 - - [06/Nov/2024:08:30:21 +0300] "GET /favicon.ico HTTP/1.1" 404 555 "http://example.com" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
192.168.1.103 - - [06/Nov/2024:08:30:22 +0300] "POST /contact HTTP/1.1" 200 678 "http://example.com/contact" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
203.0.113.15 - - [06/Nov/2024:08:30:23 +0300] "GET /admin HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
203.0.113.10 - - [06/Nov/2024:10:30:15 +0300] "POST /api/login HTTP/1.1" 401 173 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
```
5) В файле nginx.log найти записи, содержащие "_/api/login_"
6) В файле nginx.log найти записи, содержащие "_POST_" и вывести код ответа
7) В директории text_processing создать файл iptables.log с содержимым
```
Nov  6 08:15:30 firewall kernel: [12345.678901] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=203.0.113.10 DST=192.168.1.100 LEN=40 TOS=0x00 PREC=0x00 TTL=235 ID=54321 PROTO=TCP SPT=45678 DPT=80 WINDOW=1024 RES=0x00 SYN URGP=0
Nov  6 08:15:35 firewall kernel: [12345.789012] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=10.0.0.5 DST=192.168.1.1 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=12345 PROTO=TCP SPT=56789 DPT=22 WINDOW=64240 RES=0x00 SYN URGP=0
Nov  6 08:15:40 firewall kernel: [UFW BLOCK] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=192.168.1.50 DST=8.8.8.8 LEN=84 TOS=0x00 PREC=0x00 TTL=64 ID=0 DF PROTO=UDP SPT=54321 DPT=53 LEN=64
Nov  6 08:15:45 firewall kernel: [UFW BLOCK] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=203.0.113.20 DST=192.168.1.100 LEN=40 TOS=0x00 PREC=0x00 TTL=235 ID=54322 PROTO=TCP SPT=45679 DPT=443 WINDOW=1024 RES=0x00 SYN URGP=0
Nov  6 08:15:50 firewall kernel: [12346.012345] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=192.168.1.101 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=38282 DF PROTO=ICMP TYPE=8 CODE=0 ID=1234 SEQ=1
Nov  6 08:15:55 firewall kernel: [12346.123456] iptables: IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=10.0.0.10 DST=192.168.1.100 LEN=52 TOS=0x00 PREC=0x00 TTL=127 ID=25588 DF PROTO=TCP SPT=49206 DPT=3389 WINDOW=8192 RES=0x00 SYN URGP=0
Nov  6 10:35:22 firewall kernel: [UFW BLOCK] IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=203.0.113.20 DST=192.168.1.1 LEN=40 TOS=0x00 PREC=0x00 TTL=249 ID=54321 PROTO=TCP SPT=45678 DPT=22 WINDOW=1024 RES=0x00 SYN URGP=0
```
8) В файле iptables.log найти записи, которые содержат "_UFW BLOCK_" и вывести только ip адрес источника
9) В директории text_processing создать файл git.log с содержимым
```
6f9a6b7 (Alice Smith 2024-11-06 10:45:30 +0300) Fix critical security vulnerability in user authentication
a1b2c3d (Bob Johnson 2024-11-06 10:50:15 +0300) Merge branch 'feature/new-api' into develop
2e3f4g5 (Charlie Brown 2024-11-06 11:15:45 +0300) Implement new dashboard layout
7h8i9j0 (Diana Prince 2024-11-06 11:30:20 +0300) Optimize database queries for better performance
k1l2m3n (Alice Smith 2024-11-06 12:00:00 +0300) Add unit tests for core modules
4o5p6q7 (Fiona Gallagher 2024-11-06 12:30:10 +0300) Update dependencies to latest versions
r8s9t0u (George Costanza 2024-11-06 13:15:30 +0300) Refactor user management service
1v2w3x4 (Hannah Baker 2024-11-06 14:00:45 +0300) Add support for multi-language content
y5z6a7b (Alice Smith 2024-11-06 14:45:20 +0300) Implement caching mechanism for API
```
10) В файле git.log найти записи содержащие "_Alice Smith_" и вывести только первое поле
# Часть 2: Пользователи и группы
1) Создать группы developers, designers, managers и admins
2) Создать пользователей jdoe, asmith, mjackson, kchen, rgarcia
3) Добавить пользователей
- mjackson в группу admins
- jdoe, kchen, rgarcia в группу developers
- asmith - в группу designers
4) Вывести из файла /etc/passwd только имена созданных пользователей
5) Вывести из файла /etc/group названия и состав добавленных групп
6) Задать пользователям пароли
7) Добавить пользователя asmith в группу managers
8) С помощью команды id получить информацию о пользователе asmith и вывести его первичную группу
9) Выполнить команду ```sudo getent shadow``` и из ее вывода получить имена добавленных в п2 пользователей и хеши их паролей
# Часть 3: Права доступа
1) В домашней директории создать директорию magento
2) В директории magento создать директории media, code и styles
3) В директории code создать файл index.php с содержимым
```
<?php
phpinfo();
?>
```
4) В директории styles создать файл main.css с содержимым
```
h1 {
    color: #333; /* Цвет текста */
    text-align: center; /* Выравнивание по центру */
}
```
5) В директории magento создать файл index.html с содержимым
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Подключаем CSS -->
</head>
<body>
    <header>
        <h1>Welcome!</h1>
        <h2>e-commerce site</h2>
    </header>
```
6) Сделать владельцем файла index.html пользователя mjackson, а группой владельцев - группу developers
7) Сделать владельцем файла styles/main.css пользователя asmith, а группой владельцев - группу designers
8) Сделать владельцем файла code/index.php пользователя rgarcia, а группой владельцев - группу admins
