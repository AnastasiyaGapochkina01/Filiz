# Часть 1
1) В директории text_processing создать файл long-long-file
2)  В директории text_processing создать файл create_file.sh с содержимым
 ```
#!/bin/bash
for i in {1..100}; do echo "$(hostname) $(date +%M:%S)" >> long-long-file; sleep 2; done &
```
3) Сделать файл create_file.sh исполняемым для всех
4) Выполнить команду ```./create_file.sh```
5) Найти в выводе команды ps процесс create_file.sh и вывести только его pid и comm
6) Посмотреть содержимое файла long-long-file
7) С помощью wc посчитать количество строк в фале long-long-file
8) Убить процесс create_file.sh
9) В директории text_processing создать директорию temp
10) В директории temp создать файл files.sh с содержимым
```
#!/bin/bash
for i in {1..12}
do
  touch "res-$i.txt"
  echo "Created at $(date +%s)" >> res-$i.txt
done
```
11) Сделать файл файл files.sh исполняемым для всех
12) Выполнить команду ```./files.sh```
13) В директории temp найти все файлы, в имени которых есть .txt и посчитать их количество
14) Удалить из директории temp все файлы, в имени которых есть res
15) Перейти в директорию text_processing и выполнить команду ```ps -eo pid,comm >> processes```
16) Посчитать количество строк в файле processes
17) В файле processes найти все строки, содержащие kworker и посчитать их количество
# Часть 2
1) Проверить, существует ли файл /proc/devices, если да, то найти в нем строки содержащие tty
2) Проверить, существует ли файл /proc/modules, если да, то найти в нем строки содержащие watchdog
3) Проверить, существует ли файл /proc/keys, если да, то найти в нем строки содержащие user и вывести для них первый и пятый столбцы
4) В директории text_processing создать файл iptables-save.log с содержимым
```
Jan 12 10:15:23 server kernel: Iptables: INPUT packet died: IN=eth0 OUT= MAC=00:0c:29:2f:09:b6:00:50:56:c0:00:08:08:00 SRC=192.168.1.100 DST=192.168.1.1 LEN=52 TOS=0x00 PREC=0x00 TTL=128 ID=18156 DF PROTO=TCP SPT=49273 DPT=80 WINDOW=64240 RES=0x00 SYN URGP=0
Jan 12 10:16:45 server kernel: Iptables: Invalid packet: IN=eth0 OUT= MAC=00:0c:29:2f:09:b6:00:50:56:c0:00:08:08:00 SRC=10.0.0.5 DST=192.168.1.1 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=54321 PROTO=TCP SPT=12345 DPT=22 WINDOW=65535 RES=0x00 SYN URGP=0
Jan 12 10:17:12 server kernel: Iptables: Ping detected: IN=eth0 OUT= MAC=00:0c:29:2f:09:b6:00:50:56:c0:00:08:08:00 SRC=172.16.0.10 DST=192.168.1.1 LEN=84 TOS=0x00 PREC=0x00 TTL=64 ID=0 DF PROTO=ICMP TYPE=8 CODE=0 ID=5678 SEQ=1
Jan 12 10:20:15 firewall kernel: Iptables: ACCEPT IN=eth0 OUT= MAC=00:0c:29:2f:09:b6:00:50:56:c0:00:08:08:00 SRC=203.0.113.10 DST=192.168.1.5 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=12345 DF PROTO=TCP SPT=33046 DPT=80 WINDOW=64240 RES=0x00 SYN URGP=0
```
5) В файле iptables-save.log найти строку, в которой SRC=10.0.0.5 и вывести для нее время и сообщение

<img width="1067" alt="image" src="https://github.com/user-attachments/assets/67c5f689-433d-4635-9264-1aaf86cad654" />

6) В директории text_processing создать файл apache_access.log с содержимым
```
167.158.76.119 - - [12/Jan/2025:02:58:01 +0000] "0 /path/to/resource4.html HTTP/1.1" 300 10265 "http://www.example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
113.254.63.37 - -  "0 /path/to/resource2.html HTTP/1.1" 500 2722 "http://www.example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
197.84.181.42 - - [11/Jan/2025:20:47:01 +0000] "0 /path/to/resource5.html HTTP/1.1" 200 2451 "http://www.example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
131.104.171.132 - - [11/Jan/2025:20:38:01 +0000] "0 /path/to/resource7.html HTTP/1.1" 500 5333 "http://www.example.com/" "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
245.72.233.240 - - [11/Jan/2025:17:58:01 +0000] "0 /path/to/resource5.html HTTP/1.1" 500 4612 "http://www.example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
63.38.69.110 - -  "0 /path/to/resource1.html HTTP/1.1" 600 7657 "http://www.example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
145.75.159.177 - -  "0 /path/to/resource2.html HTTP/1.1" 300 5286 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
185.232.26.6 - - [12/Jan/2025:07:00:01 +0000] "0 /path/to/resource5.html HTTP/1.1" 500 10154 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
242.95.161.88 - - [11/Jan/2025:15:00:01 +0000] "0 /path/to/resource5.html HTTP/1.1" 200 8888 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
```
7) В файле apache_access.log найти строки, содержащие resource5 и вывести для них ip и код ответа

 <img width="1125" alt="image" src="https://github.com/user-attachments/assets/9ff0ba13-ef52-4f43-8228-63234a56b4b2" />

8) В директории text_processing создать файл php-error.log с содержимым
```
[36.252.172.99] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 68
[12-Jan-2025 08:08:01] [110.1.177.127] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 60
[11-Jan-2025 13:45:01] [137.117.251.143] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 11
[10.195.86.143] PHP Fatal error:  Uncaught Error: Call to undefined function nonexistent_function() in /var/www/html/functions.php:83
[96.187.17.230] PHP Fatal error:  Uncaught Error: Call to undefined function nonexistent_function() in /var/www/html/functions.php:48
[11-Jan-2025 17:10:01] [235.4.34.31] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 65
[11-Jan-2025 10:57:01] [86.145.153.114] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 97
[11-Jan-2025 22:55:01] [27.89.66.40] PHP Parse error:  syntax error, unexpected 'if' (T_IF) in /var/www/html/broken_script.php on line 73
[82.133.144.106] PHP Notice:  Undefined variable: undefined_var in /var/www/html/script.php on line 81
```
9) В файле php-error.log найти строки, содержащие Uncaught Error и вывести первый столбец
10) В файле php-error.log найти строки, содержащие Undefined variable и вывести в какой строке ошибка

<img width="806" alt="image" src="https://github.com/user-attachments/assets/b8d35408-570c-4d0c-adf4-eefa7f6071bd" />
