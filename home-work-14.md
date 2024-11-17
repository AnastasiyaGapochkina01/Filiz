# Часть 1
1) В домашней директории создать директорию laravel
2) В директории laravel создать следующую структуру каталогов
```
│
├── data/
│
├── docker/
│   ├── mysql/
│   │   ├── Dockerfile
│   │   └── my.cnf
│   │
│   ├── nginx/
│   │   ├── Dockerfile
│   │   └── default.conf
│   │
│   └── php-fpm/
│       └── Dockerfile
├── src/ 
│   ├── app/ 
│   ├── bootstrap/
│   ├── database/
│   ├── public/
├── .env
├── docker-compose.yml
└── README.md        
```
3) В директории laravel создать директорию confs
4) Скопировать файлы my.cnf, default.conf в директорию confs
5) Переименовать директорию src в code
6) Переименовать директорию src/database в db-data
7) Переместить файл docker-compose.yml в директорию docker
8) В директории src/public создать директорию dist
9) Скопировать всю директорию src в директорию data
10) Удалить директорию src
# Часть 2
1) В директории text_processing создать файл nginx_access.log с содержимым
```
208.110.70.42 - - [16/Nov/2024:11:36:50 +0000] "GET /restore.php HTTP/1.1" 404 153 "-" "-"
82.157.247.165 - - [16/Nov/2024:11:54:06 +0000] "HEAD /invoker/EJBInvokerServlet HTTP/1.1" 404 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
82.157.247.165 - - [16/Nov/2024:11:54:12 +0000] "PATCH /jmx-console/HtmlAdaptor?action=inspectMBean&name=jboss.system:type=ServerInfo HTTP/1.1" 404 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
82.157.247.165 - - [16/Nov/2024:11:54:18 +0000] "HEAD /invoker/JMXInvokerServlet HTTP/1.1" 404 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
82.157.247.165 - - [16/Nov/2024:11:54:24 +0000] "HEAD /web-console/ServerInfo.jsp HTTP/1.1" 404 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
192.71.233.142 - - [16/Nov/2024:12:17:10 +0000] "GET /api HTTP/1.1" 404 125 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0"
179.43.169.162 - - [16/Nov/2024:12:24:03 +0000] "GET / HTTP/1.1" 200 6681 "-" "Hello World"
179.43.169.162 - - [16/Nov/2024:12:24:03 +0000] "POST / HTTP/1.1" 200 6681 "-" "Hello World"
141.98.11.178 - - [16/Nov/2024:12:27:37 +0000] "GET / HTTP/1.1" 200 2464 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
199.45.155.68 - - [16/Nov/2024:10:53:24 +0000] "PRI * HTTP/2.0" 400 157 "-" "-"
```
2) Найти в файле nginx_access.log записи, содержащие PATCH и PRI
3) Найти в файле nginx_access.log записи, содержащие PATCH и POST и вывести только ip
4) В директории text_processing создать файл disk-usage.log с содержимым
```
2024-11-17_04:26:58 Disk usage on tech-preprod is greater than 3: current value is 42
2024-11-17_04:26:58 Disk usage on tech-stage is greater than 2: current value is 42
2024-11-17_04:26:58 Disk usage on tech-preprod is greater than 4: current value is 57
2024-11-17_04:26:58 Disk usage on tech-prod is greater than 4: current value is 64
2024-11-17_04:26:58 Disk usage on tech-preprod is greater than 0: current value is 23
2024-11-17_04:26:58 Disk usage on tech-prod is greater than 4: current value is 99
2024-11-17_04:26:58 Disk usage on tech-stage is greater than 5: current value is 10
2024-11-17_04:26:58 Disk usage on tech-preprod is greater than 9: current value is 79
2024-11-17_04:26:58 Disk usage on tech-prod is greater than 6: current value is 71
2024-11-17_04:26:58 Disk usage on tech-preprod is greater than 3: current value is 22
```
5) В файле disk-usage.log найти записи, относящиеся к tech-prod и вывести значение current value
6) В выводе команды ```dpkg --list``` найти cron и curl и вывести название пакета и его версию
7) Из вывода команды ```dpkg-architecture``` получить значение переменных DEB_HOST_ARCH и DEB_TARGET_GNU_CPU
8) Из вывода команды ```locale``` вывести значение LC_MESSAGES
9) Из вывода команды ```lslocks``` вывести PID и PATH
10) В файле /etc/sysctl.conf найти значения net.ipv4.tcp_syncookies и kernel.sysrq
# Часть 3
1) Создать пользователей malek, bern, kassey и will
2) Создать группы postgres и mysql
3) Добавить пользователей kassey и bern в группу mysql, а malek и will - в группу postgres
4) Задать пользователям malek, bern, kassey и will пароли
5) В домашней директории создать директорию users, в ней директории malek, bern, kassey и will
6) Установить владельцем и группой владельцев на каждую директорию malek, bern, kassey и will одноименного пользователя и группу
7) В директории users создать файл restricted.txt и установить права так, чтобы только владелец мог читать и писать в файл
8) В директории users создать диреткорию private_dir и установить права так, тобы только владелец мог читать, записывать и выполнять в ней
9) Создать группу devs и добавить в нее пользователей malek, bern, kassey и will
10) В директории users создать файл main и предоставить группе devs права на чтение, запись и исполнение этого файла
