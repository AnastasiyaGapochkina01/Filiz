# Часть 1
1) В домашней директории создать файл date-logging.sh с содержимым
```
#!/bin/bash

worker() {
  LOGFILE="worker_out.log"

  while true; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Запись времени" >> "$LOGFILE"
    echo "Записано время в $LOGFILE"

    sleep 30
  done
}
worker &
WORKER_PID=$!

while true; do
  echo "Worker is $WORKER_PID"
  sleep 5
done
```
2) Сделать файл date-logging.sh исполняемым для всех
3) Выполнить команду ```./date-logging.sh > /dev/null &```
4) Проверить, появился ли в домашней директори файл worker_out.log
5) Вывести worker_out.log на экран
6) Найти id процессов date-logging.sh
7) Найти в директории /proc директории, которые соответствуют id процессов date-logging
8) В одной из директорий, найденных в пункте 5 найти файл cmdline и вывести его содержимое на экран
9) Вывести на экран только id и пользователя от которого запущены процессы date-logging
10) Запустить htop (если не запускается, то установить командой ```sudo apt install -y htop```). Есть ли в списке процессов date-logging? Самостоятельно найти информацию как делать поиск процесса в htop и найти date-logging в htop
11) Убить процессы date-logging
# Часть 2: Обработка текста
1) В директории text_processing создать файл myconfig.conf с содержимым
```
app_name = MyApplication
app_version = 1.0.0
log_level = debug

[database]
db_host = localhost
db_port = 5432
db_user = admin
db_password = secret
db_name = my_database

[server]
host = 0.0.0.0
port = 8080
timeout = 30

[cache]
cache_enabled = true
cache_ttl = 3600

[security]
enable_https = true
ssl_cert_file = /etc/ssl/certs/mycert.pem
ssl_key_file = /etc/ssl/private/mykey.key

[api]
api_key = YOUR_API_KEY_HERE
api_timeout = 15

[notifications]
email_enabled = true
sms_enabled = false

[allowed_ips]
ip_list = 192.168.1.1,192.168.1.2,10.0.0.1

[integrations]
service_a_url = https://api.service-a.com/v1/
service_b_url = https://api.service-b.com/v1/

[additional]
feature_x_enabled = false
max_connections = 100
```
2) В файле myconfig.conf найти значение директивы ssl_cert_file и проверить, существует ли файл, который там указан
3) В файле myconfig.conf найти значение max_connections. Изменить его на 250
4) В файле myconfig.conf найти адреса интеграций - занчения service_a_url и service_b_url
5) Сделать копию файла myconfig.conf с новым именем myconfig.conf.bk
6) В файле myconfig.conf найти значение директивы ip_list
7) Из файла myconfig.conf вывести все строки, начинающиеся с db
8) Проверить, существует ли директория /var/log
9) Проверить, существует ли директория grub в директории /boot; если да, то проверить существует ли в /boot/grub файл grub.cfg; если да, то в файле /boot/grub/grub.cfg найти строки вида ```linux   /boot/vmlinuz```
10) Выполнить команду ```sudo systemctl list-units``` и найти в ее выводе все строки, содержащие running
11) В директории text_processing создать файл serivice_app.log с содержимым
```
2024-12-18 10:00:01 INFO  Starting MyApplication version 1.0.0
2024-12-18 10:00:02 DEBUG Initializing database connection to localhost:5432
2024-12-18 10:00:03 WARNING Database connection took longer than expected
2024-12-18 10:00:05 ERROR Failed to connect to the database: connection refused
2024-12-18 10:00:06 INFO  Retrying database connection...
2024-12-18 10:00:08 INFO  Successfully connected to the database
2024-12-18 10:00:10 DEBUG Fetching user data from the database
2024-12-18 10:00:11 INFO  User data fetched successfully
2024-12-18 10:00:15 WARNING High memory usage detected
2024-12-18 10:00:20 ERROR Unable to send notification email to user@example.com
2024-12-18 10:00:25 INFO  Shutting down MyApplication gracefully
2024-12-18 10:00:26 INFO  Application stopped successfully
```
12) В файле serivice_app.log найти все сообщения, содержащие ERROR и WARNING
13) Из файла serivice_app.log вывести все записи, содержащие информацию о подключении к базе данных
14) Из файла serivice_app.log вывести запись с предупреждениями о высоком использовании памяти (High memory usage detected)
15) В файле serivice_app.log айти и вывести строку с последним сообщением об ошибке
