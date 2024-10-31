# Часть 1: Пользователи
1) Создать пользователей user_{1,2,3,4,5}
2) Вывести из файла /etc/passwd только имена созданных пользователей (grep)
3) Добавить группы workers; teachers; students, для этого выполнить команды
```
sudo groupadd workers
sudo groupadd teachers
sudo groupadd students
```
4) Вывести из файла /etc/group только названия добавленных групп
5) Пользователей user_1 и user_2 добавить в группу workers
6) Пользователей user_3, user_4, user_5 добавить в группу students
7) Создать пользователя mentor3 и добавить в группу teachers
8) Вывести на экран состав групп workers; teachers; students
9) Задать пароли для всех пользователей (```passwd user_1```)
10) С помощью команды id получить информацию о пользователе mentor3 и вывести только список его групп

# Часть 2:
1) В директории text_processing создать файл application.log с содержимым
```
2024-10-31 04:43:12,591 - DEBUG - User logged in
2024-10-31 04:43:12,591 - INFO - Warning: Low memory
2024-10-31 04:43:12,591 - WARNING - Data retrieved successfully
2024-10-31 04:43:12,591 - DEBUG - Critical error: System failure
2024-10-31 04:43:12,591 - ERROR - Application started
2024-10-31 04:43:12,591 - WARNING - Application started
2024-10-31 04:43:12,591 - DEBUG - Warning: Low memory
2024-10-31 04:43:12,591 - INFO - Application started
2024-10-31 04:43:12,592 - ERROR - Application started
2024-10-31 04:43:12,592 - DEBUG - Application started
2024-10-31 04:43:12,592 - WARNING - Critical error: System failure
2024-10-31 04:43:12,592 - ERROR - Critical error: System failure
2024-10-31 04:43:12,592 - DEBUG - Application shutting down
2024-10-31 04:43:12,592 - DEBUG - Application shutting down
2024-10-31 04:43:12,592 - ERROR - Data retrieved successfully
2024-10-31 04:43:12,592 - INFO - Data retrieved successfully
2024-10-31 04:43:12,592 - ERROR - Warning: Low memory
2024-10-31 04:43:12,592 - WARNING - Error: Failed to connect to the database
2024-10-31 04:43:12,592 - INFO - Critical error: System failure
2024-10-31 04:43:12,592 - DEBUG - Request for data received
2024-10-31 04:43:12,592 - INFO - Critical error: System failure
2024-10-31 04:43:12,592 - INFO - Error: Failed to connect to the database
```

<img width="716" alt="image" src="https://github.com/user-attachments/assets/cc2e5940-e69d-4698-ad02-a5e913fad395">

2) Найти в файле application.log все записи уровня ERROR (уровень это та часть строки, которая записана большими буквами)
3) Найти в файле application.log записи о неудачном подключении к базе данных (поиск попробовать по database)
4) Найти в файле application.log все записи уровня WARNING и вывести для них время и сообщение
5) Найти в файле application.log все записи, в которых упомнается memory и вывести их уровень
6) В директории text_processing создать файл app_metrics с содержимым
```
# Application Metrics Log
# metric_name: metric_value
total_requests: 150
successful_requests: 145
failed_requests: 5
average_response_time_ms: 120
max_response_time_ms: 350
min_response_time_ms: 80
memory_usage_mb: 256
cpu_usage_percent: 75
total_requests: 200
successful_requests: 195
failed_requests: 5
average_response_time_ms: 110
memory_usage_mb: 270
cpu_usage_percent: 80
```
7) В файле app_metrics найти метрики, относящиеся к cpu
8) Из файла app_metrics получить _занчение_ метрики average_response_time_ms
9) В файле app_metrics найти метрики, относящиеся к response_time и из них вывести _значение_ метрики max_response_time
10) Выполнить команду uptime и вывести значения load average

<img width="447" alt="image" src="https://github.com/user-attachments/assets/358232d5-d3d0-49c2-a2fd-a08ff70c126f">

11) Выполнить команду lastlog и вывести имена пользователей у который столбец Latest содержит дату

<img width="790" alt="image" src="https://github.com/user-attachments/assets/af329ebb-b341-4cda-83d9-9b378a99242d">
