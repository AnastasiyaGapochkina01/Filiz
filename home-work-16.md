# Часть 1
1) Создать пользователей ansible, grafana, prometheus и cadvisor
2) Создать группу monitoring
3) Добавить пользователей grafana, prometheus и cadvisor в группу monitoring
4) В директории /opt создать директорию prom-stack
5) В директории prom-stack создать директории prometheus-config, grafana-config и cadvisor-data
6) Назначить владельцем и группой владельцев директории prometheus-config пользователя prometheus
7) Назначить владельцем и группой владельцев директории grafana-config пользователя grafana
8) Назначить владельцем и группой владельцев директории cadvisor-data пользователя cadvisor
9) В директории prom-stack создать файл compose.yaml
10) Назначить группой владельцев файла compose.yaml группу monitoring, а владельцем - root
11) Забрать у others все права на файл compose.yaml
12) В директории prom-stack создать файл install-prom-stack
13) Сделать файл install-prom-stack исполняемым только для владельца. У группы и всех остальных не должно быть никаких прав на этот файл
14) В директории prom-stack создать файл .acl
15) Установить права на файл .acl так, чтобы владелец мог читать и записывать, а группа и остальные пользователи только читать
16) В директории prom-stack создать файл config.ini
17) Установить права доступа на файл config.ini так, чтобы его можно было только читать
18) В директории prom-stack создать директорию tmp
19) Установить полные права для всех категорий пользователей на директорию tmp
20) Установить права доступа на файл config.ini так, чтобы владелец мог записывать в него
# Часть 2
1) Выполнить команду ```sudo systemctl list-units --type=service```, в выводе найти journald.service
2) Выяснить, есть ли в директории /etc файл service, если есть - найти в нем сервисы shell и whois; вывести из найденных строк 1 и третий столбцы
3) Выяснить, есть ли в директории /etc файл ca-certificates.conf, если есть - найти в нем строки, содержащие COMODO
4) В файле /proc/vmstat найти значение numa_other
5) В файле /proc/filesystems найти все записи, содержащие ext
6) В директории text_processing создать файл apache2_access_log с содержимым
```
192.168.1.100 - - [24/Nov/2024:14:35:12 +0300] "GET /index.html HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
10.0.0.5 - john [24/Nov/2024:14:35:15 +0300] "POST /login HTTP/1.1" 302 0 "http://example.com/login" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
172.16.0.10 - - [24/Nov/2024:14:35:18 +0300] "GET /images/logo.png HTTP/1.1" 304 0 "http://example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
192.168.1.101 - alice [24/Nov/2024:14:35:20 +0300] "GET /api/users HTTP/1.1" 200 2345 "-" "PostmanRuntime/7.32.3"
10.0.0.6 - - [24/Nov/2024:14:35:22 +0300] "GET /styles/main.css HTTP/1.1" 200 5678 "http://example.com/index.html" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
192.168.1.102 - - [24/Nov/2024:14:35:25 +0300] "GET /favicon.ico HTTP/1.1" 404 345 "http://example.com/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
172.16.0.11 - bob [24/Nov/2024:14:35:28 +0300] "PUT /api/update HTTP/1.1" 200 123 "-" "curl/7.68.0"
10.0.0.7 - - [24/Nov/2024:14:35:30 +0300] "GET /blog HTTP/1.1" 301 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
192.168.1.103 - - [24/Nov/2024:14:35:33 +0300] "GET /products?category=electronics HTTP/1.1" 200 8901 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
172.16.0.12 - - [24/Nov/2024:14:35:36 +0300] "OPTIONS /api HTTP/1.1" 200 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
```
7) В файле apache2_access_log найти строки, содержащие адрес 192.168.1.102
8) В файле apache2_access_log найти строки, содержащие PostmanRuntime и вывести 1 и 3 поле
9) В директории text_processing создать файл catalina.out с содержимым
```
24-Nov-2024 14:45:12.357 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deploying web application directory [/opt/tomcat/webapps/ROOT]
24-Nov-2024 14:45:12.567 INFO [dev] org.apache.catalina.startup.HostConfig.deployDirectory Deployment of web application directory [/opt/tomcat/webapps/ROOT] has finished in [209] ms
24-Nov-2024 14:45:12.569 INFO [main] org.apache.coyote.AbstractProtocol.start Starting ProtocolHandler ["http-nio-8080"]
24-Nov-2024 14:45:12.577 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [298] milliseconds
24-Nov-2024 14:46:23.456 EXCEPTION [http-nio-8080-exec-1] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
 Note: further occurrences of HTTP request parsing errors will be logged at DEBUG level.
java.lang.IllegalArgumentException: Invalid character found in method name. HTTP method names must be tokens
    at org.apache.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:407)
    at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:263)
    at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
    at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:891)
    at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1784)
    at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
    at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
    at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
    at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
    at java.base/java.lang.Thread.run(Thread.java:829)
24-Nov-2024 14:47:34.567 INFO [main] org.apache.catalina.core.StandardServer.await A valid shutdown command was received via the shutdown port. Stopping the Server instance.
24-Nov-2024 14:47:34.568 INFO [main] org.apache.coyote.AbstractProtocol.pause Pausing ProtocolHandler ["http-nio-8080"]
24-Nov-2024 14:47:34.569 INFO [dev] org.apache.catalina.core.StandardService.stopInternal Stopping service [Catalina]
24-Nov-2024 14:47:34.571 INFO [main] org.apache.coyote.AbstractProtocol.stop Stopping ProtocolHandler ["http-nio-8080"]
24-Nov-2024 14:47:34.573 INFO [main] org.apache.coyote.AbstractProtocol.destroy Destroying ProtocolHandler ["http-nio-8080"]
```
10) В файле catalina.out найти записи, содержащие [dev] и вывести для найденных строк время
11) В файле catalina.out найти EXCEPTION
12) В директории text_processing создать файл audit.log с содержимым
```
type=SYSCALL msg=audit(1700917512.123:1000): arch=c000003e syscall=2 success=yes exit=3 a0=7fff9d7d4580 a1=0 a2=1fffffffffff0000 a3=7fff9d7d3060 items=1 ppid=1234 pid=5678 auid=1000 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=1 comm="cat" exe="/usr/bin/cat" subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key="sshd_config"
type=PATH msg=audit(1700917512.123:1000): item=0 name="/etc/ssh/sshd_config" inode=12345 dev=08:01 mode=0100644 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:etc_t:s0 objtype=NORMAL cap_fp=0000000000000000 cap_fi=0000000000000000 cap_fe=0 cap_fver=0
type=PROCTITLE msg=audit(1700917512.123:1000): proctitle=636174002F6574632F7373682F737368645F636F6E666967
type=USER_AUTH msg=audit(1700917600.456:1001): pid=1122 uid=0 auid=1000 ses=2 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 msg='op=PAM:authentication grantors=pam_unix acct="john" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'
type=USER_ACCT msg=audit(1700917600.456:1002): pid=1122 uid=0 auid=1000 ses=2 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 msg='op=PAM:accounting grantors=pam_unix,pam_permit,pam_time acct="john" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'
type=CRED_ACQ msg=audit(1700917600.456:1003): pid=1122 uid=0 auid=1000 ses=2 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 msg='op=PAM:setcred grantors=pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'
type=USER_START msg=audit(1700917600.789:1004): pid=1234 uid=0 auid=1000 ses=2 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 msg='op=PAM:session_open grantors=pam_keyinit,pam_limits,pam_systemd,pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'
type=USER_END msg=audit(1700917610.321:1005): pid=1234 uid=0 auid=1000 ses=2 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 msg='op=PAM:session_close grantors=pam_keyinit,pam_limits,pam_systemd,pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/0 res=success'
```
13) В файле audit.log найти pid=1234 и вывести чему равен type
14) В директории text_processing создать файл secure с содержимым
```
Nov 24 15:00:01 server sshd[1234]: Accepted publickey for john from 192.168.1.100 port 54321 ssh2: RSA SHA256:abcdefghijklmnopqrstuvwxyz123456789ABCDEFG
Nov 24 15:00:01 server sshd[1234]: pam_unix(sshd:session): session opened for user john by (uid=0)
Nov 24 15:05:23 server sudo:     john : TTY=pts/0 ; PWD=/home/john ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
Nov 24 15:05:23 server sudo: pam_unix(sudo:session): session opened for user root by john(uid=0)
Nov 24 15:05:23 server sudo: pam_unix(sudo:session): session closed for user root
Nov 24 15:10:45 server sshd[2345]: Failed password for invalid user admin from 10.0.0.5 port 12345 ssh2
Nov 24 15:10:47 server sshd[2345]: Failed password for invalid user admin from 10.0.0.5 port 12345 ssh2
Nov 24 15:10:49 server sshd[2345]: Failed password for invalid user admin from 10.0.0.5 port 12345 ssh2
Nov 24 15:10:49 server sshd[2345]: error: maximum authentication attempts exceeded for invalid user admin from 10.0.0.5 port 12345 ssh2 [preauth]
Nov 24 15:10:49 server sshd[2345]: Disconnecting invalid user admin 10.0.0.5 port 12345: Too many authentication failures [preauth]
Nov 24 15:15:30 server su: pam_unix(su:session): session opened for user root by jane(uid=1001)
Nov 24 15:16:02 server su: pam_unix(su:session): session closed for user root
Nov 24 15:20:15 server sshd[3456]: Accepted password for alice from 172.16.0.10 port 56789 ssh2
Nov 24 15:20:15 server sshd[3456]: pam_unix(sshd:session): session opened for user alice by (uid=0)
Nov 24 15:25:00 server sudo:    alice : TTY=pts/1 ; PWD=/home/alice ; USER=root ; COMMAND=/usr/bin/systemctl restart apache2
Nov 24 15:25:00 server sudo: pam_unix(sudo:session): session opened for user root by alice(uid=0)
Nov 24 15:25:02 server sudo: pam_unix(sudo:session): session closed for user root
Nov 24 15:30:45 server sshd[4567]: Received disconnect from 192.168.1.100 port 54321:11: disconnected by user
Nov 24 15:30:45 server sshd[4567]: Disconnected from user john 192.168.1.100 port 54321
Nov 24 15:30:45 server sshd[1234]: pam_unix(sshd:session): session closed for user john
```
15) В файле secure найти Failed password и вывести время
