# Часть 1
1) В директории text_processign создать файл traefik.log с содержимым
```
192.168.1.100 - - [21/Nov/2024:06:45:23 +0300] "GET /api/users HTTP/1.1" 200 1532 "https://example.com" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" 0.087 "router-1" "http://backend-1:8080" 1
10.0.0.5 - admin [21/Nov/2024:06:45:24 +0300] "POST /api/orders HTTP/1.1" 201 256 "-" "PostmanRuntime/7.32.3" 0.156 "router-2" "http://backend-2:8080" 2
172.16.0.10 - - [21/Nov/2024:06:45:25 +0300] "GET /images/logo.png HTTP/1.1" 304 0 "https://example.com/home" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1" 0.012 "router-3" "http://backend-3:8080" 3
192.168.1.101 - user123 [21/Nov/2024:06:45:26 +0300] "PUT /api/profile HTTP/1.1" 200 789 "https://example.com/account" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" 0.203 "router-1" "http://backend-1:8080" 4
10.0.0.6 - - [21/Nov/2024:06:45:27 +0300] "GET /api/products?category=electronics HTTP/1.1" 200 4567 "-" "curl/7.68.0" 0.098 "router-2" "http://backend-2:8080" 5
```
<img width="957" alt="image" src="https://github.com/user-attachments/assets/e0c464fc-2295-4611-a037-ff9848c9b1bc">

2) В файле traefik.log найти строки, в которых содержится router-1 и вывести из них ip и запрос
3) В файле traefik.log найти запрос POST и вывести ip и User-Agent
4) В файле traefik.log найти запросы, у которых занчение backend соответствует backend-1
5) В директории text_processign создать файл opencart.log с содержимым
```
[2024-11-21 07:00:00] - INFO - User 'admin' logged in from IP 192.168.1.10
[2024-11-21 07:05:12] - ERROR - Failed to load module 'payment_gateway' due to missing configuration
[2024-11-21 07:10:45] - WARNING - User 'guest' attempted to access restricted page 'admin/dashboard'
[2024-11-21 07:15:30] - INFO - Order #12345 created by user 'customer1'
[2024-11-21 07:20:15] - DEBUG - Product 'Laptop' stock level updated to 50
[2024-11-21 07:00:00] - INFO - User 'salles' logged in from IP 192.168.1.14
[2024-11-21 07:25:40] - INFO - User 'john_doe' registered with email 'john@example.com'
[2024-11-21 07:30:22] - ERROR - Payment failed for order #12346 due to insufficient funds
[2024-11-21 07:35:50] - WARNING - High number of login attempts detected from IP 203.0.113.5
[2024-11-21 07:40:10] - INFO - User 'admin' updated product 'Smartphone' details
[2024-11-21 07:45:35] - DEBUG - Cache cleared for category 'Electronics'
[2024-11-21 07:50:55] - INFO - User 'jane_doe' changed password successfully
[2024-11-21 07:55:15] - ERROR - Image upload failed for product ID #567 due to invalid format
[2024-11-21 08:00:30] - WARNING - Low stock alert for product 'Headphones'
[2024-11-21 08:05:45] - INFO - Discount coupon 'BLACKFRIDAY' applied to order #12347
[2024-11-21 08:10:05] - DEBUG - Session timeout extended for user 'customer2'
```
6) В файле opencart.log найти все записи ERROR
7) В файле opencart.log найти все записи, содержащие logged и вывести для них имя пользователя и ip
8) В файле opencart.log найти все записи, содержащие order и вывести уроень лога (ERROR/INFO/...)
9) Выполнить команду mount и из ее вывода получить строку, содержащую ext4, а из нее - параметры монтирования (последний столбец, в скобках)
10) Выяснить с помощью ls и grep существует ли файл /boot/grub/grub.cfg. Если существует, то найти в нем строки с параметрами загрузки системы - это строки такого вида
```
linux   /boot/vmlinuz-5.10.0-19-amd64 root=UUID=39613585-2d42-4ead-84d3-c9e98b676084 ro net.ifnames=0 net.ifnames=0 biosdevname=0 console=ttyS0
```
11) Выяснить, существует ли в директории /etc файл rsyslog.conf. Если существует, то найти в нем Owner и Group
12) В файле /etc/ssh/sshd_config найти строку, содержащую PasswordAuthentication
13) Вывести файл /etc/ssh/sshd_config без строк, начинающихся с #

то есть иходный файл выглядит примерно так

<img width="591" alt="image" src="https://github.com/user-attachments/assets/3fc0738e-2a0a-411d-9920-3126a608ddd5">

нужно вывести 

<img width="609" alt="image" src="https://github.com/user-attachments/assets/1a11058e-6d2a-49a2-805e-0f34a607f3cb">

14) Из файла /etc/profile получить значение PATH

# Часть 2
1) Удалить пользователей
- malek, bern, kassey и will
- mbrown, dchan, sreva, pkolton, asandler, dgretta
2) Удалить группы
- chiefs, dockers, foremans
- postgres и mysql
3) Создать пользователей postgres-exporter и node-exporter
4) В директории /opt создать директорию exporters, в ней директории postgres и node
5) Назначить владельцем и группой владельцев директории postgres пользователя postgres-exporter, а node - node-exporter
6) В директории exporters создать файл run.sh
7) Сделать файл run.sh исполняемым _только_ для группы владельцев
8) Назначить группу exporters, добавить в нее postgres-exporter и node-exporter
9) Назначить группой владельцев файла run.sh группу exporters
10) В директории exporters создать директорию data, в ней директории pg_data и node_data
11) Назначить группой владельцев директории data группу exporters, а владельцем - root
12) Назначить postgres-exporter владельцем и группой владельцев директории pg_data
13) Назначить node-exporter владельцем и группой владельцев директории node_data
14) В директории exporters создать файл .env, назначить root владельцем и группой владельцев 
15) Назначить файлу .env права так, чтобы читать и писать мог только владелец, а все остальные не могли ничего 
