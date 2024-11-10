# Часть 1: Работа с текстом
1) В директории text_processing создать файл python.log с содержимым
```
2024-11-09 08:00:01,123 - myapp - INFO - The application is running.
2024-11-09 08:00:01,456 - myapp - DEBUG - Configuration initialization...
2024-11-09 08:00:01,789 - myapp - INFO - Database connection...
2024-11-09 08:00:02,012 - myapp - WARNING - Database is not responding, retry after 5 seconds.
2024-11-09 08:00:07,345 - myapp - ERROR - Failed to connect to the database: Timeout expired.
2024-11-09 08:00:07,678 - myapp - INFO - Shutdown of the application.
```
2) Из файла python.log вывести все записи, содержащие ERROR и вывести время и сообщение об ошибке
3) Из файла python.log вывести записи, содержащие Database (в любом регистре) и получить из них только уровень (INFO/WARNNING/ERROR)
4) В директории text_processing создать файл searchd.log с содержимым
```
2024-11-09 08:00:01: [INFO] Sphinx 3.0.3 started
2024-11-09 08:00:01: [INFO] listening on 127.0.0.1:9306
2024-11-09 08:00:01: [INFO] listening on 127.0.0.1:9312
2024-11-09 08:00:01: [INFO] using config file '/home/user/sphinxdata/sphinx.conf'
2024-11-09 08:00:02: [DEBUG] starting indexer process
2024-11-09 08:00:02: [INFO] indexing index 'my_index'
2024-11-09 08:00:02: [INFO] collected 5000 documents, 1.2 MB
2024-11-09 08:00:02: [INFO] sorted 0.5 Mhits, 100.0% done
2024-11-09 08:00:02: [INFO] total indexed documents: 5000
2024-11-09 08:00:02: [INFO] total time spent indexing: 2.3 sec
2024-11-09 08:00:03: [WARNING] failed to open pid_file '/home/user/sphinxdata/searchd.pid'
2024-11-09 08:00:04: [ERROR] unable to connect to MySQL server at 'localhost': Access denied for user 'root'@'localhost' (using password: YES)
2024-11-09 08:00:05: [INFO] searchd stopped
```
5) В файле searchd.log найти записи, содержащие listening и вывести хост и порт
6) В файле searchd.log найти записи, содержащие ERROR
7) В файле searchd.log найти записи, содержащие DEBUG или WARNING и вывести для них только время
8) В директории text_processing создать файл rabbitmq.log с содержимым
```
2024-11-09 08:00:01.123 [info] <0.1234.0> Starting RabbitMQ 3.9.0 on Erlang 24.0
2024-11-09 08:00:01.456 [info] <0.1234.0> Server startup complete
2024-11-09 08:00:02.789 [info] <0.1235.0> Supervisor 'rabbit@localhost' started
2024-11-09 08:00:03.012 [warning] <0.1236.0> Connection failed: TCP connection to 127.0.0.1:5672 refused
2024-11-09 08:00:04.345 [error] <0.1237.0> Failed to open file /var/lib/rabbitmq/mnesia/rabbit@localhost/queues/queue1: No such file or directory
2024-11-09 08:00:05.678 [info] <0.1238.0> New client connection from 192.168.1.10:54321
2024-11-09 08:00:06.901 [info] <0.1239.0> Message published to exchange 'my_exchange'
2024-11-09 08:00:07.234 [critical] <0.1240.0> Node rabbit@localhost is shutting down
```
9) В файле rabbitmq.log найти записи critical и error
10) В файле rabbitmq.log найти записи об exchange и вывести их уровень
11) Получить из вывода команды free -h размер доступной памяти (available)
12) Получить из вывода команды lscpu количество ядер (CPU(s))
# Часть 2
1) Создать группы chiefs, dockers, foremans
2) Создать пользователей mbrown, dchan, sreva, pkolton, asandler, dgretta
3) Добавить пользователей asandler, dgretta в группу foremans
4) Добавить пользователей mbrown, pkolton в группу dockers
5) Добавить пользователей dchan, sreva в группу chiefs
6) Добавить пользователя talman и добавить его во все группы, созданные в задании 1
7) Из файла /etc/group вывести только состав добавленных групп
8) Выполнить команду ```id talman``` и получить их ее вывода список групп пользователя talman
# Часть 3
1) В домашней директории создать директорию trade_port
2) В директории trade_port создать директории security_office, cargo_operations_sector, control_area
3) В директории trade_port создать файл main.list с содержимым
```
1. **Harbor Area**
   - **Description**: The area for safe anchorage of vessels waiting to enter the port.
   - **Responsible Party**: Harbor Master
2. **Berths and Terminals**
   - **Description**: Locations where vessels dock for loading and unloading cargo.
   - **Responsible Party**: Terminal Operations Manager

   2.1 **Container Terminal**
   - **Description**: Specialized area equipped with cranes for handling containers.
   - **Responsible Party**: Container Terminal Supervisor
3. **Warehousing Facilities**
   - **Description**: Open and covered storage areas for temporary cargo storage.
   - **Responsible Party**: Warehouse Manager
```
4) Сделать владельцем файла main.list пользователя root, а группой - chiefs
5) В директории security_office создать файл security.list с содержимым
```
# Security Policies and Access Control List

# User Roles and Access Levels
1. **Admin**
   - Access Level: Full Control
   - Permissions: 
     - Manage users and groups
     - Configure system settings
     - Access all resources

2. **Manager**
   - Access Level: Limited Control
   - Permissions:
     - View reports
     - Manage team members
     - Approve requests

3. **User**
   - Access Level: Basic Access
   - Permissions:
     - View personal data
     - Submit requests
     - Access assigned resources

4. **Guest**
   - Access Level: Restricted Access
   - Permissions:
     - View public information
     - No modification rights
```
6) Сделать владельцем файла security.list пользователя sreva, а группой - chiefs
7) В директории cargo_operations_sector создать файл cargo.list с содержимым
```
# Cargo Shipment List

# General Information
- Shipment ID: SHP-2024-001
- Date: 2024-11-10
- Origin: Port of Los Angeles, USA
- Destination: Port of Shanghai, China
- Carrier: Ocean Freight Co.

# Cargo Details
1. **Cargo Item**
   - Description: Electronic Components
   - Quantity: 500 units
   - Weight: 1000 kg
   - Volume: 5 m³
   - Dimensions (LxWxH): 1.2m x 1.0m x 0.5m
   - Packaging Type: Carton Box
   - Hazardous Material: No

2. **Cargo Item**
   - Description: Automotive Parts
   - Quantity: 300 units
   - Weight: 1500 kg
   - Volume: 7 m³
   - Dimensions (LxWxH): 1.5m x 1.2m x 0.8m
   - Packaging Type: Palletized
   - Hazardous Material: No

3. **Cargo Item**
   - Description: Chemicals
   - Quantity: 200 liters
   - Weight: 250 kg
   - Volume: 0.25 m³
   - Packaging Type: Drum
   - Hazardous Material: Yes (UN Number: 1234)

# Shipping Requirements
- Shipping Method: Sea Freight
- Estimated Departure Date: 2024-11-15
- Estimated Arrival Date: 2024-12-05

# Handling Instructions
- **Electronic Components**:
  - Keep dry and avoid exposure to moisture.
  - Handle with care; avoid dropping or rough handling.

- **Automotive Parts**:
  - Store in a cool, dry place.
  - Secure on pallets to prevent shifting during transport.

- **Chemicals**:
  - Follow all safety protocols for hazardous materials.
  - Ensure proper labeling and documentation during transport.

# Documentation Required
- Bill of Lading (BOL)
- Commercial Invoice
- Packing List
- Safety Data Sheet (SDS) for Chemicals

# Contact Information
- Shipper Contact:
  Name: John Doe
  Phone: +1 (555) 123-4567
  Email: johndoe@example.com

- Receiver Contact:
  Name: Jane Smith
  Phone: +86 (21) 9876-5432
  Email: janesmith@example.com
```
8) Сделать владельцем файла cargo.list пользователя asandler, а группой - dockers
9) В файле cargo.list найти записи о Quantity и вывести только значение
10) В директории control_area создать файл control.list с содержимым
```
# Control Measures and Policies List

# General Information
- Document ID: CTRL-2024-001
- Date: 2024-11-10
- Prepared by: Quality Assurance Team
```
11) Сделать владельцем файла control.list пользователя dchan, а группой - foremans
12) Сделать владельцем директории trade_port пользователя talman
13) Вывести полученную структуру каталогов командой tree
