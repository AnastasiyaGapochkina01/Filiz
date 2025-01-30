# Часть 1 
1) В директории text_processing создать файл api_response с содержимым
```
<response>
  <status>success</status>
  <data>
    <item>
      <id>1</id>
      <name>Target 1</name>
      <description>Controller of DNS</description>
    </item>
    <item>
      <id>2</id>
      <name>Target 2</name>
      <description>Controller of GW</description>
    </item>
  </data>
  <metadata>
    <timestamp>2025-01-30T06:00:00+03:00</timestamp>
    <count>2</count>
  </metadata>
</response>
```
2) С помощью grep и регулярных выражений получить из файла api_response
- все значения тегов ```<id>```
- все имена целей (содержимое тегов ```<name>```)
- описания всех элементов (содержимое тегов ```<description>```)
- количество элементов из метаданных (содержимое тега ```<count>```)
3) В директории text_processing создать файл m2.log с содержимым
```
[2025-01-30 04:56:43] main.INFO : The user has successfully logged in [] []
[2025-01-30 04:57:12] main.WARNING: Attempt to access a non-existent page [] []
[2025-01-30 04:58:01] main.ERROR: Error during payment processing {"order_id":"10001","payment_method":"credit_card"} []
[2025-01-30 04:59:30] main.DEBUG: API request: GET /products {"params":{"category":"electronics","limit":10}} []
[2025-01-30 05:00:15] main.CRITICAL: Critical error in the Inventory module {"module":"Magento_Inventory","exception":"OutOfStockException"} []
```
4) С помощью grep и регулярных выражений получить из файла m2.log все уровни ошибок

<img width="629" alt="image" src="https://github.com/user-attachments/assets/30acacd3-286c-4084-8068-279f4bc1064f" />

5) В директории text_processing создать файл audit.log с содержимым
```
type=CRED_DISP msg=audit(1737696084.384:13): pid=2250 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:setcred grantors=pam_permit acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=USER_ACCT msg=audit(1737696093.513:14): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:accounting grantors=pam_permit acct="anestesia" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=USER_CMD msg=audit(1737696093.513:15): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='cwd="/etc/promtail" cmd=6C73202F7661722F6C6F672F61756469742F exe="/usr/bin/sudo" terminal=pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=CRED_REFR msg=audit(1737696093.513:16): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:setcred grantors=pam_permit acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=USER_START msg=audit(1737696093.513:17): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:session_open grantors=pam_permit,pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=USER_END msg=audit(1737696093.517:18): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:session_close grantors=pam_permit,pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=CRED_DISP msg=audit(1737696093.517:19): pid=2485 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:setcred grantors=pam_permit acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=USER_ACCT msg=audit(1737696109.427:20): pid=2496 uid=1000 auid=1000 ses=1 subj=unconfined msg='op=PAM:accounting grantors=pam_permit acct="anestesia" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'^]UID="anestesia" AUID="anestesia"
type=SYSCALL msg=audit(1737696144.264:35): arch=c000003e syscall=257 success=yes exit=3 a0=ffffff9c a1=7f17b5c4715e a2=80000 a3=0 items=1 ppid=619 pid=2511 auid=1000 uid=1000 g
id=1000 euid=0 suid=0 fsuid=0 egid=1000 sgid=1000 fsgid=1000 tty=pts0 ses=1 comm="sudo" exe="/usr/bin/sudo" subj=unconfined key="passwd"^]ARCH=x86_64 SYSCALL=openat AUID="anestesia" UID="anestesia" GID="anestesia" EUID="root" SUID="root" FSUID="root" EGID="anestesia" SGID="anestesia" FSGID="anestesia"
type=CWD msg=audit(1737696144.264:35): cwd="/etc/promtail"
type=PATH msg=audit(1737696144.264:35): item=0 name="/etc/passwd" inode=29389 dev=fe:02 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0^]OUID="root" OGID="root"
type=PROCTITLE msg=audit(1737696144.264:35): proctitle=7375646F00617564697463746C002D6C
type=SYSCALL msg=audit(1737696144.264:36): arch=c000003e syscall=257 success=yes exit=5 a0=ffffff9c a1=7f17b5c4715e a2=80000 a3=0 items=1 ppid=619 pid=2511 auid=1000 uid=1000 gid=1000 euid=0 suid=0 fsuid=0 egid=1000 sgid=1000 fsgid=1000 tty=pts0 ses=1 comm="sudo" exe="/usr/bin/sudo" subj=unconfined key="passwd"^]ARCH=x86_64 SYSCALL=openat AUID="anestesia" UID="anestesia" GID="anestesia" EUID="root" SUID="root" FSUID="root" EGID="anestesia" SGID="anestesia" FSGID="anestesia"
type=CWD msg=audit(1737696144.264:36): cwd="/etc/promtail"
type=PATH msg=audit(1737696144.264:36): item=0 name="/etc/passwd" inode=29389 dev=fe:02 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0^]OUID="root" OGID="root"
```
6) С помощью grep и регулярных выражений получить из файла audit.log
- все типы сообщений
- все значения acct
- все UID
- все значения terminal

<img width="830" alt="image" src="https://github.com/user-attachments/assets/6752f03b-8536-4556-93cb-f329134ec350" />

7) В директории text_processing создать файл iptables_adv.log с содержимым
```
Jan 30 07:01:23 server kernel: [122972.300408] Iptables: Ping detected: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:91 SRC=192.168.1.100 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=23020 PROTO=ICMP TYPE=8 CODE=0 ID=33602 SEQ=1
Jan 30 07:02:15 server kernel: [122974.123456] Iptables: Invalid packet: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:92 SRC=10.0.0.5 DST=192.168.1.1 LEN=40 TOS=0x00 PREC=0x00 TTL=233 ID=54321 PROTO=TCP SPT=12345 DPT=80 WINDOW=1024 RES=0x00 SYN URGP=0
Jan 30 07:03:30 server kernel: [122975.987654] Iptables: INPUT packet died: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:93 SRC=172.16.0.10 DST=192.168.1.1 LEN=52 TOS=0x00 PREC=0x00 TTL=117 ID=62266 DF PROTO=TCP SPT=57413 DPT=22 WINDOW=8192 RES=0x00 SYN URGP=0
Jan 30 07:04:45 server kernel: [122976.246810] Iptables: FORWARD packet died: IN=eth0 OUT=eth1 MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:94 SRC=192.168.2.50 DST=8.8.8.8 LEN=84 TOS=0x00 PREC=0x00 TTL=63 ID=0 DF PROTO=ICMP TYPE=8 CODE=0 ID=6404 SEQ=1
Jan 30 07:05:10 server kernel: [122977.135790] Iptables: Ping detected: IN=eth0 OUT= MAC=00:64:d9:36:7b:d7:00:24:2d:a6:e2:43:08:95 SRC=192.168.1.101 DST=192.168.1.1 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=23021 PROTO=ICMP TYPE=8 CODE=0 ID=33603 SEQ=2
```
8) С помощью grep и регулярных выражений получить из файла iptables_adv.log
- все MAC-адреса
- все ip-адреса SCR
- все ip-адреса DST
- все значения PROTO
- все строки, в которых SEQ=1

<img width="877" alt="image" src="https://github.com/user-attachments/assets/b1066a84-7968-4aa5-a83d-c845116888a1" />

# Часть 2
1) В директории text_processing создать директорию diagnostic
2) В директории diagnostic создать файл collecting.sh с содержимым
```
#!/bin/bash

check_ram() {
    while true; do
        free_ram=$(free -m | awk '/^Mem:/{print $7}')
        echo "$(hostname) $(date '+%Y-%m-%d %H:%M:%S') INFO Free RAM size - ${free_ram}" >> ram_log.txt
        sleep 60
    done
}

get_network_settings() {
    ip addr show > network_settings.txt
    sleep 60
}

check_ram &

get_network_settings &

wait
```
3) Сделать файл collecting.sh исполняемым
4) Находясь в директори diagnostic выполнить команду ```./collecting.sh &```
5) Проверить, появились ли в директории diagnostic файлы network_settings.txt и ram_log.txt. Если да, то
- из файла network_settings.txt получить ip-адрес машины

<img width="700" alt="image" src="https://github.com/user-attachments/assets/bee37481-fcbe-46f6-bb46-82b5c7d0ba1c" />

- из файла ram_log.txt получить первый и последний столбцы (регулярки можно не использовать)

6) Найти все процессы collecting.sh и для них вывести пользователя, от имени которого они запущены (user), pid, pcpu, comm, stat
7) Приостановить один из процессов collecting и проверить изменился ли его статус
8) Возобновить процесс collecting
9) Убить все процессы collecting
# Часть 3
1) В домашней директории создать директорию projects
2) В директории projects создать файл create_prj.sh с содержимым
```
#!/bin/bash

project_name=$1

mkdir $project_name
cd $project_name

mkdir cmd pkg internal api docs tests

mkdir cmd/$project_name
mkdir internal/app internal/pkg
mkdir pkg/models pkg/utils
mkdir api/handlers api/middleware
mkdir docs/swagger
mkdir tests/unit tests/integration

touch main.go
touch README.md
touch .gitignore
```
3) Сделать файл create_prj.sh исполняемым
4) Создать пользователей service, devuser и qauser
5) Проверить, существуют ли группы devs и testers, если нет, то создать их
6) Добавить пользователя qauser в группу testers
7) Добавить пользователя devuser в группы testers и devs
8) В директории projects выполнить команду ```./create_prj.sh cross-pro```
9) Проверить, появилась ли в директории projects директория cross-pro. Если да, то вывести на экран ее структуру с помощью ```tree```
10) Назначить владельцем директории cross-pro/tests пользователя qauser, а группой владельцев группу testers
11) Назначить владельцем директории cross-pro пользователя devuser, а группой владельцев группу devs
12) Назначить владельцем всех директорий и файлов в директории cross-pro ***кроме tests*** пользователя devuser, а группой владельцев группу devs
13) Назначить права на файл main.go так, чтобы владелец имел полные права на него, группа могла только читать, а все остальные не имели никаких прав
14) Назначить права на директорию docs так, чтобы все категории пользователей имели полные права
15) Назначить права на файл README.md так, чтобы владелец мог читать и записывать, группа могла читать и записывать, а все остальные не имели никаких прав
16) Назначить права на директорию internal так, чтобы владелец имел полные права, а группа и все остальные не имели никаких прав
17) В директории projects создать директорию backups
18) Скопировать директорию cross-pro в директорию backups
19) Переименовать директорию backups/cross-pro в backups/01_cross-pro_bkp
20) Назначить владельцем директории backups пользователя service, а группой владельцев - root
