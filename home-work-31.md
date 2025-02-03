# Часть 1
1) В директории tex_processing создать файл notes.txt с содержимым
```
## Date: February 3, 2025

### Tasks
- TODO: Prepare a project report 
- Hold a meeting with the team - DONE
- Learn a new tool for the job - IN PROGRESS 
- TODO: Complete the project report
- Schedule a team meeting - DONE
- TODO: Research new tools for productivity

### Ideas:
- Develop a new marketing strategy.
- Conduct a survey among customers to improve the service.

### Reminders:
- Don't forget about your friend's birthday on February 15th.
- Check your mail for important emails.

### Useful links:
- [Project documentation](https://example.com )
- [Productivity Tools](http://example.com )
```
2) С помощью grep и регулярных выражений получить из notes.txt
- все url
-  все задачи в статусе TODO
3) В директории tex_processing создать файл logfile.log с содержимым
```
2025-02-01 10:00:00 - INFO - Application started successfully.
2025-02-01 10:05:23 - WARNING - Low disk space on drive C:.
2025-02-01 10:15:45 - ERROR - Failed to connect to the database 10.3.1.5:3306. Retrying...
2025-02-01 10:20:10 - INFO - Successfully connected to the database 10.3.1.5:3306.
2025-02-01 11:00:00 - INFO - User logged in: user@example.com.
2025-02-01 11:05:30 - INFO - Data export completed successfully.
2025-02-01 11:30:15 - WARNING - High memory usage detected.
2025-02-01 12:00:00 - INFO - Application stopped.
```
4) С помощью grep и регулярных выражений получить из logfile.log
- дату
- время
- log level
- ip-адреса
- email
5) В директории tex_processing создать файл users.list с содержимым
```
Green.D - dgreen@gmail.com services: [bookstore (checkout), printing_house (statistics)]
John.S - john.smith@example.com services: [cafe (order), library (renewal)]
Alice.W - alicewl@example.com services: [theater (tickets)]
Charlie.B - charliebr@example.com services: [supermarket (delivery)] - +19153456783
Hank.P - hank.peters@example.com services: [car_rental (reservations)]
Eve.R - eve.rivers@example.com services: [restaurant (reservations), bakery (orders)] - +19184329674
```
6) С помощью grep и регулярных выражений получить из users.list
- все email
- все номера телефонов
- все services
7) В директории text_processing создать файл new_iptables с содержимым
```
Feb 03 08:00:00 server kernel: Iptables: Ping detected: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:91 SRC=192.168.1.10 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=124 ID=23020 PROTO=ICMP TYPE=8 CODE=0 ID=33602 SEQ=2462
Feb 03 08:00:01 server kernel: Iptables: Invalid packet: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:91 SRC=192.168.1.20 DST=192.168.1.1 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=12345 PROTO=TCP SPT=1234 DPT=80
Feb 03 08:00:02 server kernel: Iptables: INPUT packet died: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:91 SRC=192.168.1.30 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=51 ID=18374 DF PROTO=UDP SPT=53 DPT=53
Feb 03 08:00:03 server kernel: Iptables: FORWARD packet died: IN=eth1 OUT=eth0 MAC=d4:f9:f5:c3:f7:c8 SRC=10.0.0.5 DST=10.0.0.10 LEN=100 TOS=0x00 PREC=0x00 TTL=128 ID=13461 PROTO=TCP SPT=443 DPT=80
Feb 03 08:00:04 server kernel: Iptables: HACKERS detected from IP 64.55.11.2 - IN=eth0 OUT=MATCH MAC=d4:f9:f5:c3:f7:c8 SRC=64.55.11.2 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=50 ID=78901 PROTO=TCP SPT=6666 DPT=22
```
8) С помощью grep и регулярных выражений получить из файла new_iptables
- все сообщения
- все mac адреса
- все типы PROTO
- все значения DST

<img width="960" alt="image" src="https://github.com/user-attachments/assets/e7ead0ba-6611-47dc-9d63-ae7ec1aedee2" />

# Часть 2
1) В директории text_processing/diagnostic создать файл get_infov2.sh с содержимым
```
#!/bin/bash

get_pci() {
  echo "===> DEVICES <===" >> devices.log
  pci_dev=$(lspci)
  echo "$(date +"%Y-%m-%d %H:%M:%S") [$(hostname)] INFO $pci_dev" >> devices.log
  sleep 60
}

get_dsks() {
  devices=$(lsblk | grep disk | awk '{print "Name: " $1, - "Size: " $4}')
  echo "$(date +"%Y-%m-%d %H:%M:%S") [$(hostname)] INFO $devices" >> devices.log
  sleep 60
}

get_mem() {
  mem=$(lsmem | grep 'Total online memory')
  echo "$(date +"%Y-%m-%d %H:%M:%S") [$(hostname)] INFO $mem" >> devices.log
  sleep 60
}

get_pci &
get_dsks &
get_mem &

wait
```
2) Сделать файл get_infov2.sh исполняемым
3) Находясь в директори diagnostic выполнить команду ```./get_infov2.sh &```
4) Проверить, появился ли файл devices.log в директории diagnostic. Если да, то любым способом найти в файле devices.log
- значение Total online memory
- строку, содержащую VGA
- все строки, содержащие bridge
- все значения log level

<img width="649" alt="image" src="https://github.com/user-attachments/assets/6e535d6b-c23d-4fb7-a216-9ead9169d952" />

- строку, содержащую информацию про диск (disks) и вывести из найденной строки значения Name и Size
5) Найти все процессы get_infov2.sh и посчитать их количество
6) Выбрать один из процессов get_infov2.sh и для него
- вывести только user и pid
- вывести ppid,pid,comm
- найти в диектории /proc директорию этого процесса и в ней найти
  - файл syscall и вывести его на экран
  - файл smaps и найти в нем VmFlags
  - файл stat и получить из него второй и третий столбцы
- приостановить процесс и проверить его статус. снова найти файл stat и получить из него второй и третий столбцы
- возобновить процесс и проверить его статус. снова найти файл stat и получить из него второй и третий столбцы
7) Убить все процессы get_infov2.sh
# Часть 3
1) Перейти в директорию projects (она в домашней директории)
2) Содать файл prepare.sh с содержимым
```
#!/bin/bash

sudo useradd kait
sudo useradd vi

if [ $? -eq 0 ]; then
    echo "Users kait и vi created" >> prepare_out.log
else
    echo "Users creation error" >> prepare_out.log
    exit 1
fi

mkdir -p ./bookstore/{src,docs,tests,bin,lib}

mkdir -p ./bookstore/src/{models,views,controllers}

mkdir -p ./bookstore/tests/{unit,integration}

if [ $? -eq 0 ]; then
    echo "Project created" >> prepare_out.log
else
    echo "Project creation error" >> prepare_out.log
    exit 1
fi
```
3) Сделать файл prepare.sh исполняемым
4) Выполнить ```./prepare.sh```
5) Проверить, появились ли в projects файл prepare_out.log и директория bookstore. Если да, то вывести структуру директории bookstore c помощью tree
6) Проверить, появились ли пользователи kait и vi
7) Удалить файл prepare_out.log
8) В директории bookstore создать файл app.py и сделать его исполняемым только для владельца
9) Назначить владельцем директории tests пользователя kait
10) Назначить владельцем директории src пользователя vi
11) Назначить владельцем всех директорий, вложенных в src пользователя vi
12) Назначить права на директорию bin так, чтобы только владелец и группа имели полный доступ, а все остальные не имели никаких прав
13) Назначить права на директорию docs так, чтобы владелец и группа не имели никаких прав, а все остальные имели полные права
14) Назначить права на директорию src и все вложенные в нее директории так, чтобы владалец имел все права, группа могла только читать, а все остальные не имели никаких прав
15) Назначить владельцем  всех директорий, вложенных в tests пользователя kait
