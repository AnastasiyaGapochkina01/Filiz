# Часть 1
1) В директории text_processing создать директорию files
2) В директории files создать файл create_infofiles.sh с содержимым
```
#!/bin/bash

for i in {1..5}; do
    filename="info-$i.txt"
    username=$(whoami)
    hostname=$(hostname)
    date=$(date +"%Y-%m-%d")
    time=$(date +"%H:%M:%S")
    echo "$username $hostname $date $time" > "$filename"
done
```
3) Сделать файл create_infofiles.sh исполняемым только для владельца
4) Выполнить команду ```./create_infofiles.sh```
5) В директории files найти все файлы, в именах которых есть .txt и посчитать их количество
6) В директории files выполнить команду ```ps -eo ppid,pid,pri,comm >> some_processess```
7) Посчитать количество строк в файле some_processess
8) В файле some_processess найти процесс systemd и вывести второй столбец
9) В директории files удалить все файлы
10) В директории files создать файл check_nginx.sh с содержимым
```
#!/bin/bash

while true; do
    count=$(pgrep -c nginx)

    echo "$(date +"%Y-%m-%d %H:%M:%S") - Nginx processes: $count" >> nginx_count

    sleep 5
done &
```
11) Сделать файл check_nginx.sh исполняемым и выполнить ```./check_nginx.sh```
12) Найти в выводе команды ps процесс check_nginx и вывести ppid, pid и comm
13) Проверить, появился ли в директории files файл nginx_count. Если да, то вывести его содержимое
14) Убить два процесса nginx worker
15) Проверить, изменились ли записи в nginx_count
16) Убить процесс check_nginx
17) В директории files создать файл mem.sh с содержимым
```
#!/bin/bash

while true; do
    free_memory=$(free -h | grep 'Mem:' | awk '{print $4}')

    #echo "$(date +"%Y-%m-%d %H:%M:%S") - Free memory: $free_memory" >> memory_free

    sleep 5
done &
```
18) Сделать файл mem.sh исполняемым и выполнить ```./mem.sh```
19) Найти в выводе команды ps процесс mem.sh
20) Вывести для процесса mem.sh параметры pid,comm,stat,pcpu
21) Убить процесс mem.sh
22) В директории files создать файл gen_child.sh с содержимым
```
#!/bin/bash

# Функция для запуска дочернего процесса
start_child() {
    echo "Запуск дочернего процесса с PID: $$"
    sleep 10000  # Имитация работы дочернего процесса
}

# Запуск трех дочерних процессов в фоновом режиме
for i in {1..3}; do
    start_child &
done

# Ожидание завершения всех дочерних процессов
wait

echo "Все дочерние процессы завершены."
```
23) Сделать файл gen_child.sh исполняемым и выполнить ```./gen_child.sh```
24) С помощью ps найти все процессы gen_child и посчитать их количество
25) С помощью ps найти все процессы sleep и посчитать их количество
26) Убить все процессы gen_child
# Часть 2
1) В директории text_processing создать файл messages с содержимым
```
Jan 16 06:01:31 dos-26 kernel: [    5.638686] audit: type=1400 audit(1737007286.187:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=274 comm="apparmor_parser"
Jan 16 06:01:31 dos-26 kernel: [    5.645322] audit: type=1400 audit(1737007286.187:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=274 comm="apparmor_parser"
Jan 16 06:01:31 dos-26 kernel: [    5.704355] input: PC Speaker as /devices/platform/pcspkr/input/input4
Jan 16 06:01:31 dos-26 kernel: [    5.722940] input: QEMU Virtio Tablet as /devices/pci0000:00/0000:00:02.0/virtio0/input/input5
Jan 16 06:01:31 dos-26 kernel: [    5.883020] iTCO_vendor_support: vendor-support=0
Jan 16 06:01:31 dos-26 kernel: [    5.953831] iTCO_wdt: Intel TCO WatchDog Timer Driver v1.11
Jan 16 06:01:31 dos-26 kernel: [    5.953963] iTCO_wdt: Found a ICH9 TCO device (Version=2, TCOBASE=0x0660)
Jan 16 06:01:31 dos-26 kernel: [    5.954260] iTCO_wdt: initialized. heartbeat=30 sec (nowayout=0)
```
2) В файле messages найти строки, содержащие apparmor и вывести для них 3 и 4 столбцы
3) В директории text_processing создать файл auth.log с содержимым
```
Jan 16 06:20:31 dos-26 sshd[1196]: Received disconnect from 106.51.64.158 port 43158:11: Bye Bye [preauth]
Jan 16 06:20:31 dos-26 sshd[1196]: Disconnected from invalid user applmgr 106.51.64.158 port 43158 [preauth]
Jan 16 06:21:16 dos-26 sshd[1198]: Connection closed by authenticating user root 193.32.162.130 port 44428 [preauth]
Jan 16 06:21:26 dos-26 sshd[1200]: Invalid user billing from 106.51.64.158 port 43186
Jan 16 06:21:26 dos-26 sshd[1200]: Received disconnect from 106.51.64.158 port 43186:11: Bye Bye [preauth]
Jan 16 06:21:26 dos-26 sshd[1200]: Disconnected from invalid user billing 106.51.64.158 port 43186 [preauth]
Jan 16 06:22:21 dos-26 sshd[1203]: Invalid user zhaoa from 106.51.64.158 port 43192
Jan 16 06:22:21 dos-26 sshd[1203]: Received disconnect from 106.51.64.158 port 43192:11: Bye Bye [preauth]
Jan 16 06:22:21 dos-26 sshd[1203]: Disconnected from invalid user zhaoa 106.51.64.158 port 43192 [preauth]
Jan 16 06:23:16 dos-26 sshd[1205]: Invalid user wsj from 106.51.64.158 port 43206
Jan 16 06:23:16 dos-26 sshd[1205]: Received disconnect from 106.51.64.158 port 43206:11: Bye Bye [preauth]
Jan 16 06:23:16 dos-26 sshd[1205]: Disconnected from invalid user wsj 106.51.64.158 port 43206 [preauth]
Jan 16 06:24:11 dos-26 sshd[1214]: Invalid user gang from 106.51.64.158 port 43214
Jan 16 06:24:11 dos-26 sshd[1214]: Received disconnect from 106.51.64.158 port 43214:11: Bye Bye [preauth]
Jan 16 06:24:11 dos-26 sshd[1214]: Disconnected from invalid user gang 106.51.64.158 port 43214 [preauth]
Jan 16 06:25:01 dos-26 CRON[1298]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jan 16 06:25:01 dos-26 CRON[1298]: pam_unix(cron:session): session closed for user root
Jan 16 06:25:01 dos-26 sshd[1296]: Invalid user eliu from 106.51.64.158 port 43236
Jan 16 06:25:02 dos-26 sshd[1296]: Received disconnect from 106.51.64.158 port 43236:11: Bye Bye [preauth]
Jan 16 06:25:02 dos-26 sshd[1296]: Disconnected from invalid user eliu 106.51.64.158 port 43236 [preauth]
Jan 16 06:25:55 dos-26 sshd[1415]: Invalid user zhzhang from 106.51.64.158 port 43260
Jan 16 06:25:55 dos-26 sshd[1415]: Received disconnect from 106.51.64.158 port 43260:11: Bye Bye [preauth]
Jan 16 06:25:55 dos-26 sshd[1415]: Disconnected from invalid user zhzhang 106.51.64.158 port 43260 [preauth]
Jan 16 06:26:49 dos-26 sshd[1472]: Invalid user cr from 106.51.64.158 port 43286
Jan 16 06:26:50 dos-26 sshd[1472]: Received disconnect from 106.51.64.158 port 43286:11: Bye Bye [preauth]
Jan 16 06:26:50 dos-26 sshd[1472]: Disconnected from invalid user cr 106.51.64.158 port 43286 [preauth]
```
4) В файле auth.log найти строки, содержащие wsj и для них вывести дату и время
5) В файле auth.log найти строки, содержащие eliu и applmgr
6) В директории text_processing создать файл daemon.log с содержимым
```
Jan 16 06:15:07 dos-26 systemd[1]: Starting Daily apt upgrade and clean activities...
Jan 16 06:15:09 dos-26 systemd[1]: apt-daily-upgrade.service: Succeeded.
Jan 16 06:15:09 dos-26 systemd[1]: Finished Daily apt upgrade and clean activities.
Jan 16 06:16:24 dos-26 ntpd[507]: 83.167.27.4 local addr 10.129.0.3 -> <null>
Jan 16 06:16:27 dos-26 systemd[1]: Starting Cleanup of Temporary Directories...
Jan 16 06:16:27 dos-26 systemd[1]: systemd-tmpfiles-clean.service: Succeeded.
Jan 16 06:16:27 dos-26 systemd[1]: Finished Cleanup of Temporary Directories.
Jan 16 06:20:55 dos-26 ntpd[507]: 212.41.8.158 local addr 10.129.0.3 -> <null>
Jan 16 06:24:49 dos-26 ntpd[507]: 80.93.187.13 local addr 10.129.0.3 -> <null>
Jan 16 06:26:15 dos-26 ntpd[507]: 45.10.43.111 local addr 10.129.0.3 -> <null>
Jan 16 06:26:33 dos-26 ntpd[507]: 93.95.98.77 local addr 10.129.0.3 -> <null>
```
7) В файле daemon.log найти строки, содержащие ntpd и вывести ip

<img width="639" alt="image" src="https://github.com/user-attachments/assets/a1c11618-5c8f-43d5-b422-1e0d50d819c9" />

8) В файле daemon.log найти строки, содержащие systemd и вывести время
9) В директории text_processing создать файл cloud-init.log с содержимым
```
2025-01-16 06:01:31,927 - handlers.py[DEBUG]: start: modules-config/config-byobu: running config-byobu with frequency once-per-instance
2025-01-16 06:01:31,927 - helpers.py[DEBUG]: config-byobu already ran (freq=once-per-instance)
2025-01-16 06:01:31,927 - handlers.py[DEBUG]: finish: modules-config/config-byobu: SUCCESS: config-byobu previously ran
2025-01-16 06:01:31,927 - main.py[DEBUG]: Ran 12 modules with 0 failures
2025-01-16 06:01:31,928 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/status.json (via temporary file /var/lib/cloud/data/tmpue5kg2f3) - w: [644] 54
1 bytes/chars
```
10) В файле cloud-init.log найти строки, содержащие handlers.py и посчитать их количество
