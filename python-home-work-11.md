1) Создать файл `logs.txt` с содержимым
```
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
ERROR: Connection failed
WARNING: Disk full
ERROR: Timeout
INFO: Service started
```
Написать скрипт, который читает файл `logs.txt` и подсчитывает, сколько раз встречается слово ERROR.
2) Создать файл `web-logs` с содержимым
```
[2025-05-01] GET /index.html 200
[2025-05-10] GET /contact 404
[2025-05-02] GET /index.html 200
[2025-05-11] GET /contact 404
[2025-05-05] GET /index.html 200
[2025-05-04] GET /contact 404
[2025-05-01] GET /index.html 200
[2025-05-13] GET /contact 404
[2025-05-02] GET /index.html 200
[2025-05-10] GET /contact 404
[2025-05-01] GET /index.html 200
[2025-05-11] GET /contact 404
[2025-05-06] GET /index.html 200
```
Написать скрипт, который читает файл `web-logs` и находит все записи старше 7 дней от текущей даты.
3) Написать скрипт, который отправляет GET-запрос на URL http://httpbin.org/get и выводит статус ответа.
4) Написать скрипт, который выводит список файлов из репозитория https://github.com/AnastasiyaGapochkina01/jenkins_params_ex
5) Напишем скрипт, который на основе json сгенерирует нам inventory.yml
```
{
  "hosts": {
    "yc-compute-1": {
      "cpu": "4 cores",
      "mem": "16 GB",
      "role": "web-server",
      "os": "Ubuntu 20.04",
      "location": "Moscow, Russia"
    },
    "yc-compute-2": {
      "cpu": "8 cores",
      "mem": "32 GB",
      "role": "database-server",
      "os": "CentOS 8",
      "location": "New York, USA"
    },
    "aws-compute-1": {
      "cpu": "2 cores",
      "mem": "8 GB",
      "role": "cache-server",
      "os": "Debian 11",
      "location": "Berlin, Germany"
    },
    "gcp-compute-2": {
      "cpu": "16 cores",
      "mem": "64 GB",
      "role": "application-server",
      "os": "Windows Server 2019",
      "location": "Tokyo, Japan"
    }
  }
}
```
