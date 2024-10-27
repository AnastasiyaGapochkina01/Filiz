1) В директории text_proxessing создать файл logs.log с содержимым
```
2024-10-27 08:15:23 INFO [Server] Application started successfully
2024-10-27 08:17:45 DEBUG [UserService] User login attempt: john_doe@example.com
2024-10-27 08:17:46 INFO [UserService] User john_doe@example.com logged in successfully
2024-10-27 08:20:12 WARN [DatabaseService] High database load detected
2024-10-27 08:22:30 ERROR [PaymentService] Transaction failed for user: alice@example.com
2024-10-27 08:22:31 INFO [PaymentService] Retrying transaction for alice@example.com
2024-10-27 08:22:32 INFO [PaymentService] Transaction successful for alice@example.com
2024-10-27 08:25:00 DEBUG [CacheService] Cache hit ratio: 0.75
2024-10-27 08:35:15 INFO [BackupService] Daily backup started
2024-10-27 08:35:22 ERROR [NetworkService] Connection timeout: 192.168.1.105
2024-10-27 08:35:25 WARN [NetworkService] Retrying connection to 192.168.1.105
2024-10-27 08:35:30 INFO [NetworkService] Connection established with 192.168.1.105
2024-10-27 08:40:00 DEBUG [MemoryManager] Current memory usage: 2.5GB
2024-10-27 08:45:12 INFO [UpdateService] Checking for system updates
2024-10-27 08:45:15 INFO [UpdateService] No new updates available
2024-10-27 08:50:30 WARN [SecurityService] Multiple failed login attempts for user: eve@example.com
2024-10-27 08:50:35 ERROR [SecurityService] Account locked: eve@example.com
2024-10-27 08:55:00 INFO [MonitoringService] All systems operating normally
2024-10-27 09:00:00 INFO [SchedulerService] Running hourly tasks
2024-10-27 09:05:23 DEBUG [APIService] API request received from 10.0.0.15
2024-10-27 09:05:24 ERROR [APIService] Invalid API key from 10.0.0.15
2024-10-27 09:10:00 INFO [LoadBalancer] Traffic distribution: Server1: 40%, Server2: 35%, Server3: 25%
2024-10-27 09:15:30 WARN [DiskService] Low disk space on /dev/sda1: 85% used
2024-10-27 09:20:00 INFO [BackupService] Daily backup completed successfully
2024-10-27 09:25:45 DEBUG [CacheService] Cache invalidation triggered
2024-10-27 09:30:00 INFO [ReportGenerator] Monthly report generation started
```
2) Найти в файле logs.log строки, содержащие ERROR и вывести к какому сервису они относятся

<img width="634" alt="image" src="https://github.com/user-attachments/assets/225d6c9c-6ade-425b-a5f6-8eb6bd0ec71f">

3) Найти в файле logs.log строки, содержащие PaymentService и вывести из этих строк только email

<img width="660" alt="image" src="https://github.com/user-attachments/assets/f37ffff0-b190-494e-92aa-196444f6272b">

4) Найти в файле logs.log записи о запросах к APIService, найти ERROR и вывести ip (тут будут два grep)

<img width="601" alt="image" src="https://github.com/user-attachments/assets/416ab9d7-637f-4c1c-ac14-78e757bb9183">

5) В файле logs.log найти записи, в которых время равно 08:35 и вывести сервисы
6) Найти в файле logs.log записи о backup и вывести время, когда бэкап запустился и когда завершился
7) Из вывода команды df -Th получить файловые системы с типом ext4

<img width="550" alt="image" src="https://github.com/user-attachments/assets/29589ead-c55b-4277-bb7e-f18eddcb99e0">

8) Из вывода команды free -h получить только столбец available
9) Из вывода команды lsmem получить значение Memory block size
10) Из вывода команды lscpu получить значение Vendor ID
