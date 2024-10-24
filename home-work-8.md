1) Вывести список имен пользователей из файла /etc/passwd (имя это превое поле)
2) В директории text_processing создать файл logs с содержимым
```
# Cron logs
Oct 20 06:24:01 server1 CRON[1349677]: (user1) CMD (   /usr/bin/python3 /home/user1/update.py)
Oct 20 06:25:01 server3 CRON[1349678]: (user2) CMD (   /usr/bin/python3 /home/user2/report.py)
Oct 20 06:26:01 server2 CRON[1349679]: (root) CMD (   /usr/bin/cleanup.sh)
Oct 20 06:27:01 server3 CRON[1349680]: (user3) CMD (   /usr/bin/backup.sh)
Oct 20 06:28:01 server1 CRON[1349681]: (user4) CMD (   /usr/bin/monitor.sh)

# Error logs
Oct 20 06:30:00 server1 sshd[12345]: Failed password for invalid user admin from 192.168.0.10 port 22 ssh2
Oct 20 06:31:00 server3 sshd[12346]: Failed password for invalid user guest from 192.168.0.11 port 22 ssh2
Oct 20 06:32:00 server1 sshd[12347]: Accepted password for user2 from 192.168.0.12 port 22 ssh2
Oct 20 06:33:00 server1 sshd[12348]: Failed password for invalid user test from 192.168.0.13 port 22 ssh2

# Warning logs
Oct 20 06:35:00 server1 kernel: [123456] Warning! CPU temperature is high.
Oct 21 09:10:00 server2 kernel: [123458] Warning! High CPU usage detected on process ID 5678.
Oct 21 09:11:00 server2 systemd[1]: Warning! Service myservice.service is taking too long to start.
Oct 21 09:12:00 server2 sshd[23461]: Warning! Multiple failed login attempts from 192.168.0.25.
Oct 21 09:13:00 server2 application[34571]: Warning! Disk space on /home is below 10% remaining.

# Info logs
Oct 21 09:02:00 server2 application[34569]: INFO User1 logged in successfully.
Oct 21 09:03:00 server2 application[34570]: INFO User3 logged out.
Oct 21 09:14:00 server2 application[34572]: INFO User4 logged in successfully from 192.168.0.26.
Oct 21 09:15:00 server2 application[34573]: INFO Backup completed successfully at /backup/user4_backup.tar.gz.
Oct 21 09:16:00 server2 systemd[1]: INFO Service myservice.service started successfully.
Oct 21 09:17:00 server2 sshd[23462]: INFO User1 logged out from session on terminal pts/0.
```
3) В файле logs.txt найти все записи, которые содержат application
4) В файле logs найти записи о запусках cron на сервере server3 и вывести команду, которая запускалась (это то, что в скобках в конце)

<img width="928" alt="image" src="https://github.com/user-attachments/assets/c61ff7c3-5346-45ff-a45e-c6511dde87a1">

5) В файле logs найти запись о сервисе myservice
6) В файле logs найти все записи, содержащие ssh и вывести для них название сервера (третье поле)

<img width="714" alt="image" src="https://github.com/user-attachments/assets/b13e56a0-1b74-438f-b910-55b9d4e1e4fa">

7) В файле logs найти все записи, содержащие kernel и вывести для них шестое поле
8) В файле logs найти все записи, содержащие "Failed password" и вывести только ip

<img width="699" alt="image" src="https://github.com/user-attachments/assets/da09364f-353d-4bd5-8563-423402547b1b">

9) В файле logs.txt найти записи, содержащие "Accepted password" и вывести имя пользователя и ip

<img width="688" alt="image" src="https://github.com/user-attachments/assets/1d36804e-31b3-4257-9b1d-97c0130a3acc">

10) В файле logs.txt найти записи, содержащие "Disk space" и вывести название сервера
