# Часть 0
Ознакомиться с синтаксисом регулряных выражений - [видео](https://www.youtube.com/watch?v=PBkJIRmWynM)
# Часть 1
1) В директории text_processing создать файл employers с содержимым
```
iivanov ivanovi@tech.com +19081348639
+79755609446 vsidorov sidorovv@mai.ru chief
head of designers mpetryakova petryakovamm@tech.com
lipatovv developer +21230953853 vlipatov@tech.com
developer kfisun fisunkv@gmai.com
```
2) С помощью grep и регулярные выражения получить из файла employers все номера телефонов
3) С помощью grep и регулярные выражения получить из файла employers все e-mail
4) В директории text_processing создать файл office_inventory с содержимым
```
iivanov-pc 192.168.10.5 Linux (Debian 11)
vvpanin-pc 192.168.10.10 Windows (10)
mgeladzem-mac 192.168.10.6 MacOs (Ventura)
vfilippov-pc 192.168.10.12 Linux (Ubuntu 22.04)
osipov-laptop 192.168.10.15 Windows (8)
```
5) С помощью grep и регулярные выражения получить из файла office_inventory все ip-адреса
6) С помощью grep и регулярные выражения получить из файла office_inventory все весии операцилнных систем
7) В директории text_processing создать файл apache_error.log с содержимым
```
[Sun Jan 19 10:00:01.123456 2025] [core:error] [pid 1234:tid 140123456789824] [client 192.168.1.1:12345] Directory index forbidden by Options directive: /var/www/html/
[Sun Jan 19 10:00:02.123456 2025] [php:error] [pid 1234:tid 140123456789824] [client 192.168.1.1:12345] PHP Warning:  include(nonexistent.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 10
[Sun Jan 19 10:00:03.123456 2025] [core:error] [pid 1234:tid 140123456789824] [client 192.168.1.2:54321] File does not exist: /var/www/html/favicon.ico
[Sun Jan 19 10:00:04.123456 2025] [authz_core:error] [pid 1234:tid 140123456789824] [client 192.168.1.3:67890] AH01630: client denied by server configuration: /var/www/html/private/
[Sun Jan 19 10:00:05.123456 2025] [core:error] [pid 1234:tid 140123456789824] [client 192.168.1.4:13579] Premature end of script headers: cgi-bin/script.cgi
```
8) С помощью grep и регулярные выражения получить из файла apache_error.log ip-адрес клиента
9) С помощью grep и регулярные выражения получить из файла apache_error.log источник записи

<img width="910" alt="image" src="https://github.com/user-attachments/assets/f5defcc5-a34e-4c1d-be8a-11187067d19b" />

10) В директории text_processing создать файл add_conf.conf
```
[allowed_ips]
ip_list = 192.168.1.1,192.168.1.2,10.0.0.1

[integrations]
service_a_url = https://api.service-a.com/v1/
service_b_url = https://api.service-b.com/v1/

[additional]
feature_x_enabled = false
max_connections = 100
```
11) С помощью grep и регулярные выражения получить из файла add_conf.conf все ip-адреса
12) С помощью grep и регулярные выражения получить из файла add_conf.conf все url
# Часть 2
1) В директории text_processing создать директорию process
2) В директории process создать файл ping-sleep.sh с содержимым
```
#!/bin/bash

ping google.com > ping1.log 2>&1 &
ping bing.com > ping2.log 2>&1 &

sleep 10000 > sleep1.log 2>&1 &
sleep 15000 > sleep2.log 2>&1 &
```
3) Сделать файл ping-sleep.sh исполняемым и выполнить команду ```./ping-sleep.sh```
4) Проверить, появились ли в директории process файлы ping* и sleep*
5) С помощью ps найти все процессы ping и посчитать их количество
6) С помощью ps найти все процессы sleep и посчитать их количество
7) Для найденных процессов ping вывести ppid,pid,comm
8) В директории process создать файл master.sh с содержимым
```
#!/bin/bash

worker() {
    local name=$1
    while true; do
        echo "$name is working..." >> "${name}.log"
        sleep 5  # Задержка для имитации работы
    done
}

worker worker1 &
worker worker2 &
worker worker3 &
```
9) Сделать файл master.sh исполняемым и выполнить ```./master.sh```
10) Найти все процессы master.sh с помощью ps
11) Вывести для всех процессов master.sh pid и comm
12) Убить все процессы ping и sleep
13) Убить все процессы master.sh
