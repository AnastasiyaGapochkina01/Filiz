# Часть 1
1) В директории text_processing создать файл products с содержимым
```
Handle:Title:SKU:Location:On hand:Available:Count
product-1:Product A:PROD-A:Warehouse A:100
product-1:Product A:PROD-A:Warehouse A:50
product-2:Product B:PROD-B:Warehouse B:200
product-2:Product B:PROD-B:Warehouse B:150
product-3:Product C:PROD-C:Warehouse C:300
product-4:Product D:PROD-D:Warehouse A:400
product-4:Product D:PROD-D:Warehouse A:250
product-5:Product E:PROD-E:Warehouse B:500
product-5:Product E:PROD-E:Warehouse B:300
product-6:Product F:PROD-F:Warehouse C:600
product-6:Product F:PROD-F:Warehouse C:400
```
2) С помощью grep найти в файле products все строки, содержащие слово PROD-C
3) С помощью grep найти в файле products все строки, содержащие слово product-3 и вывести для них последний столбец
4) С помощью grep найти в файле products все строки, у которых столбец Available равен C и для них вывести первый и последний столбец
5) В директории text_processing создать файл hosts с содержимым
```
hostname,interval,timestamp,%user,%system,%memory
sel-srv1,600,2023-10-08 00:00:01 UTC,30.01,20.77,96.21
sel-srv1,600,2023-10-08 00:05:01 UTC,40.07,13.00,84.55
sel-srv1,600,2023-10-08 00:10:01 UTC,5.00,90.55,89.23
sel-srv2,600,2023-10-09 00:15:01 UTC,25.01,15.77,92.21
sel-srv3,600,2023-10-09 00:20:01 UTC,35.07,10.00,80.55
sel-srv3,600,2023-10-09 00:25:01 UTC,10.00,85.55,88.23
sel-srv2,600,2023-10-09 00:30:01 UTC,20.01,25.77,95.21
sel-srv2,600,2023-10-09 00:35:01 UTC,45.07,12.00,82.55
sel-srv3,600,2023-10-09 00:40:01 UTC,15.00,80.55,87.23
```
6) С помощью grep найти в файле hosts строки, содержащие sel-srv2 и вывести 3 столбец
7) С помощью grep найти в файле hosts строки, содержащие дату 2023-10-08
8)  В директории text_processing создать файл inventory с содержимым
```
[Compute1]
IP_Address = 192.168.1.100
Location = Datacenter A
Service_Name = Web Server

[Compute2]
IP_Address = 192.168.1.101
Location = Datacenter B
Service_Name = Database Server

[Compute3]
IP_Address = 192.168.1.102
Location = Datacenter C
Service_Name = Application Server

[Compute4]
IP_Address = 192.168.1.103
Location = Datacenter A
Service_Name = File Server

[Compute5]
IP_Address = 192.168.1.104
Location = Datacenter B
Service_Name = Mail Server
```
9) С помощью grep в файле inventory найти все хосты, которые относятся к Datacenter B
10) С помощью grep в файле inventory найти все хосты, которые относятся к Datacenter C и вывести только их ip

# Часть 2
1) В директории home_works создать директорию roles
2) В директории roles создать директории nginx, docker и файлы inventory и main.yml
3) В директории nginx создать директории handlers, tasks, vars, files
4) В директории nginx/tasks создать файл install.yml с содержимым (*!в директорию nginx НЕ ПЕРЕХОДИТЬ, ОСТАВАТЬСЯ в roles*)
```
---
- name: Install nginx
  apt:
    name: nginx
    state: stable
    update_cahce: yes
```
5) В файл inventory записать следуюущий текст
```
[webservers]
192.168.0.1
```
6) В директории nginx/handlers создать файл main.yml с содержимым
```
---
- name: Restart Nginx
  service:
    name: nginx
    state: restarted
```
7) В директории nginx/vars создать файл main.yml
8) В директории nginx/files создать файл nginx.conf с содержимым
```
user www-data;
pid /var/run/nginx.pid;

events {
        worker_connections 1024;
        # multi_accept on;
}
```
9) В директории home_works создать директорию infrastructure и переместить туда всю директорию roles
10) В директории infrastructure создать директорию tf
11) Переместить файлы inventory и main.yml и директории roles в директорию infrastructure
12) В директории infrastructure/tf создать директории aws и yandex
13) В директориях aws и yandex создать файл main.tf
14) Вывести полученную структуру директорий командой tree
