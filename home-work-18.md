# Часть 1: Работа с процессами
1) В домашней директории создать файл web_server с содержимым
```
#!/bin/bash
LOG_FILE="$HOME/web_server.log"
log_levels=("ERROR" "INFO" "WARNING" "DEBUG")
methods=("GET" "POST" "PUT" "PATCH" "OPTIONS" "DELETE")
echo "Starting web-server on $(hostname)" >> $LOG_FILE
while true
do
  sleep 5
  random_method=${methods[$RANDOM % ${#methods[@]}]}
  random_level=${log_levels[$RANDOM % ${#log_levels[@]}]}
  echo "$(date +"%Y-%d-%m [%H:%M:%S]") $random_level $random_method" >> $LOG_FILE
  sleep 5
done
```
2) Сделать файл web_server исполняемым для всех
3) Выполнить команду ```./web_server &> /dev/null &```
4) Найти id процесса web_server
5) В домашней директории найти файл web_server.log и посмотреть его содержимое
6) В директории /proc найти каталог, который соответствует найденному выше id процесса web_server
7) Убить процесс web_server
# Часть 2: Пользователи и права доступа
1) Вывести список всех пользователей из файла /etc/passwd
2) Создать пользователя peach, сделать его домашней директорией директорию /home/peach_home
3) Задать пользователю peach пароль 1111
4) Проверить, существует ли группа admin. Если существует - добавить в нее пользователя peach; если нет - создать такую группу и добавить в нее пользователя peach
5) Получить информацию о пользователе peach с помощью команды ```id```
6) В директории home_works создать директорию secret_files и назначить ее владельцем пользователя peach, а группой - admin
7) Назначить права на директорию secret_files так, чтобы все остальные не имели никаких прав доступа к ней
8) Перейти под пользователя peach (```sudo su - peach```)
9) Проверить, что пользователь peach действительно может создавать и редактировать файлы в директории secret_files:
- создать в директории secret_files файл .secret1 с содержимым
```
admin:$2y$05$m5IrWlkAmnZOLmf4LZiSvuVXaVXK8w9I8f/5RPJDjeSpQgFJD0bXO
```
- создать в директории secret_files пустой файл .secret2
- переименовать файл .secret1 в .grandsecret, а .secret2 в .secret1
- в файл .secret1 записать строку
```
admin:$2y$05$w8sbxRv34VQrnnRESpOOXONbRWcJMlTri0n/gDy5HOkeVixa26zJu
```
- выйти из под пользователя peach командой ```exit```
10) Добавить пользователя cherry в группу admin
11) Проверить, что пользователь cherry тоже имеет доступ (или не имеет?) к директории secret_files:
- создать в директории secret_files файл .cherry_secret1 с содержимым
```
cherry:$2y$05$y4maW1b9kMi.TqNytlfdpeWkJNWouaAVSPZ9sbJB0AXoenBGHZFqG
```
- создать в директории secret_files пустой файл .cherry_secret2
- переименовать файл .cherry_secret2 в .cherry_grandsecret
- добавить в файл .secret1 строку
```
cherry:$2y$05$2jOuRh6cBpAzRsiCZQP7q.RC1tzamnGmjCopEwcHaBKQWkef9SpSK
```
- выйти из под пользователя cherry командой ```exit```
# Часть 3: Работа с текстом
1) В директории text_processing создать файл employees.csv
```
ID,Name,Department,Salary
1,John Doe,Engineering,70000
2,Jane Smith,Marketing,60000
3,Bob Johnson,Sales,55000
4,Alice Davis,Engineering,80000
5,Charlie Brown,Marketing,62000
```
2) Вывести список всех сотрудников из отдела "Engineering"
3) Вывести занчение Salary всех сотрудников из отдела "Engineering"
4)  В директории text_processing создать файл products.csv
```
SKU,Product Name,Category,Price,Stock
P001,Laptop,Electronics,999.99,50
P002,Smartphone,Electronics,499.99,100
P003,Coffee Maker,Home Appliances,79.99,30
P004,T-shirt,Fashion,19.99,200
P005,Sneakers,Fashion,49.99,150
```
5) В файле products.csv найти все продукты в категории "Fashion" и вывести только их названия и цены
6) В директории text_processing создать файл orders.csv
```
OrderID,CustomerID,OrderDate,totalAmount
1001,C001,2024-01-01,$150.00
1002,C002,2024-01-02,$200.00
1003,C001,2024-01-03,$75.00
1004,C003,2024-01-04,$300.00
1005,C002,2024-01-05,$125.00
```
7) В файле orders.csv найти все заказы от клиента с ID C001 и вывести их даты и суммы
8) Из вывода команды lsipc получить строку, содержащую SHMMNI и для нее вывести значение столбца LIMIT
9) Исключить из вывода команды ```df -Th``` все строки, содержащие tmpfs и udev
10) Проверить, есть ли в директории /etc файл xattr.conf; если есть - найти в нем строки, содержащие trusted
11) Проверить, есть ли в директории /etc файл rpc; если есть - найти в нем строки, содержащие yppasswdd или selection_svc и вывести для них 1 и 2 столбцы
12) Из файла /etc/os-release получить значение VERSION_CODENAME и VERSION_ID
13) Проверить, есть ли в директории /etc файл adduser.conf; если есть - найти в нем значение DSHELL и GROUPHOMES  
