# Часть 1: Пользователи и права доступа
1) Создать пользователей elastic, rabbitmq и kafka
2) Создать группы brokers и search
3) Добавить rabbitmq и kafka в группу brokers, а пользователя elastic в группу search
4) В директории /opt создать директорию nosql-data
5) В директории nosql-data создать
- файл rabbit.conf
- файл kafka-topic.cnf
- файл elasticsearch.conf
- директорию confs
6) Переместить файлы rabbit.conf, kafka-topic.cnf, elasticsearch.conf в директорию confs
7) В директории nosql-data создать
- директорию rabbitmq-data
- директорию kafka-data
- директорию elastic-data
8) Назначить владельцем директории rabbitmq-data пользователя rabbitmq, а группой brokers
9) Назначить владельцем директории kafka-data пользователя kafka, а группой brokers
10) Назначить владельцем директории elastic-data пользователя elastic, а группой search
11) Создать группу data и добавить в нее пользователей elastic, rabbitmq и kafka
12) Назначить права на директорию nosql-data так, чтобы полный доступ имелся у группы, а у владельцев и всех остальных был доступ только на чтение
13) Назначить группой владельцев директории nosql-data группу data
14) Создать пользователя robin с домашней директорией /home/sherwood
15) Назначить пользователю robin пароль
# Часть 2: Процессы
1) Выполнить команду ```sleep 100000```
2) Найти id процесса sleep
3) В директории /proc найти каталог, который соответствует найденному выше id процесса sleep
4) Вывести пользователя из-под которого запущен процесс sleep
5) Убить процесс sleep
# Часть 3
1) В директории text_processing создать файл processes с содержимым
```
root         491  0.0  0.0   6744  2764 ?        Ss   18:06   0:00 /usr/sbin/cron -f
message+     492  0.0  0.1   7860  4316 ?        Ss   18:06   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         494  0.0  1.7 1318632 72144 ?       Ssl  18:06   0:00 /usr/bin/gitlab-runner run --config /etc/gitlab-runner/config.toml --working-directory /home/gitlab-runner --service gitlab-runner --user gitlab-runner
anestes+     495  0.2  0.5 1238504 22720 ?       Ssl  18:06   0:00 /usr/local/go/bin/go run server.go
root         498  0.0  0.1 220796  6416 ?        Ssl  18:06   0:00 /usr/sbin/rsyslogd -n -iNONE
ntp          505  0.0  0.0  74496  3800 ?        Ssl  18:06   0:00 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 105:111
root         508  0.0  0.1  13572  6836 ?        Ss   18:06   0:00 /lib/systemd/systemd-logind
root         511  0.0  1.2 1801512 51824 ?       Ssl  18:06   0:00 /usr/bin/containerd
root         515  0.0  0.0   5844  1664 tty1     Ss+  18:06   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         517  0.0  0.0   5476  2232 ttyS0    Ss+  18:06   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,57600,38400,9600 ttyS0 vt220
root         520  0.0  0.5 108732 21484 ?        Ssl  18:06   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         546  0.0  0.1  13352  7044 ?        Ss   18:06   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         565  0.0  0.0  56380  1600 ?        Ss   18:06   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data     566  0.0  0.0  56752  3444 ?        S    18:06   0:00 nginx: worker process
www-data     567  0.0  0.0  56752  3444 ?        S    18:06   0:00 nginx: worker process
root         572  0.2  2.0 1920604 83816 ?       Ssl  18:06   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root         617  0.0  0.0      0     0 ?        I    18:06   0:00 [kworker/u4:4-flush-254:0]
root         618  0.0  0.0      0     0 ?        I    18:06   0:00 [kworker/u4:5]
anestes+     837  0.0  0.1 1526432 6140 ?        Sl   18:06   0:00 /tmp/go-build2666644712/b001/exe/server
root         842  0.0  0.2  14276  8432 ?        Ss   18:09   0:00 sshd: anestesia [priv]
anestes+     845  0.1  0.2  15184  8512 ?        Ss   18:09   0:00 /lib/systemd/systemd --user
anestes+     846  0.0  0.0 166544  2560 ?        S    18:09   0:00 (sd-pam)
anestes+     865  0.0  0.1  14276  4780 ?        S    18:09   0:00 sshd: anestesia@pts/0
anestes+     866  0.1  0.1   8168  5024 pts/0    Ss   18:09   0:00 -bash
anestes+     871  0.0  0.0   9756  3276 pts/0    R+   18:09   0:00 ps aux
```
2) В файле processes найти все строки, содержащие nginx и вывести только первое и последнее поля
3) В директории text_processing создать файл multi_nginx.conf с содержимым
```
 server {
        listen 80;
        server_name site1.example.com;
        root /var/www/site1/public;

        location / {
            index index.html index.htm index.php;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php7.4-fpm.sock; # Убедитесь, что версия PHP соответствует установленной
        }
    }

    server {
        listen 80;
        server_name site2.example.com;
        root /var/www/site2/public;

        location / {
            index index.html index.htm index.php;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        }
    }

    server {
        listen 80;
        server_name site3.example.com;
        root /var/www/site3/public;

        location / {
            index index.html index.htm index.php;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        }
    }

    # Повторите блок server для оставшихся сайтов (site4 до site25)
    
    server {
        listen 80;
        server_name site25.example.com;
        root /var/www/site25/public;

        location / {
            index index.html index.htm index.php;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        }
    }
}
```
4) Найти в файле multi_nginx.conf все значения server_name
5) Проверить, существует ли в директории /etc/rc3.d файл S01cron, если да, то найти в нем значение PIDFILE и проверить существует ли этот файл
6) Проверить, существует ли в директории /etc файл mime.types, если да, то найти в нем text/html
7) Проверить, существует ли в директории /proc файл partitions если да, то вывести из него значения столбца name
8) Проверить, существует ли в директории /proc файл cpuinfo, если да, то проверить какой у него размер. После этого открыть файл командой cat. Есть ли данные?
9) Проверить, существует ли в директории /proc файл crypto, если да, то найти в нем все строки, содержащие name
10) Проверить, существует ли в директории /boot/grub/locale файл ru.mo, если да, то определить его размер и какие права ему заданы
11) В выводе команды ```sudo dmesg``` найти все записи, содержащие NET
