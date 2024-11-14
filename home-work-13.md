# Часть 1
1) В домашней директории создать директорию ansible, в ней - roles, в roles - monitoring-server 
2) В директории monitoring-server создать следующую структуру файлов и директорий
```
.
├── README.md
├── defaults
│   └── main.yml
├── files
│   └── etc
│       └── monitoring
│           ├── compose.yaml
│           ├── config
│           │   └── alertmanager.yml
│           ├── grafana
│           │   └── datasource.yml
│           └── prometheus
│               ├── prometheus.yml
│               └── secure_alerts.yml
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml
```
3) В директории roles создать директорию part-monitoring-server
4) Скопировать из директории monitoring-server директорию tasks в part-monitoring-server
5) В директории part-monitoring-server создать директорию files
6) Скопировать из директории monitoring-server/files/etc файл compose.yaml в директорию part-monitoring-server/files
7) Переместить директорию monitoring-server/templates в директорию part-monitoring-server
8) В директории part-monitoring-server/templates создать файл env.j2
9) В директории monitoring-server удалить директорию tests
10) Переименовать директорию monitoring-server/files/etc/monitoring в prom-stack
# Часть 2
1) В директории text_processing создать файл postgres.log с содержимым
```
2024-11-14 08:00:00.123 UTC [12345]: [1-1] user=postgres db=mydb LOG:  connection received: host=127.0.0.1 port=5432
2024-11-14 08:00:01.456 UTC [12345]: [1-2] user=postgres db=mydb LOG:  connection authorized: user=postgres database=mydb
2024-11-14 08:00:03.012 UTC [12345]: [2-1] user=postgres db=app LOG:  statement: SELECT * FROM users;
2024-11-14 08:00:03.345 UTC [12345]: [2-2] user=postgres db=mydb LOG:  duration: 0.123 ms
2024-11-14 08:00:02.789 UTC [12345]: [1-3] user=postgres db=app LOG:  disconnection: session time: 0:00:02.345 user=postgres database=app host=127.0.0.1 port=5432
2024-11-14 08:00:04.678 UTC [12345]: [3-1] user=postgres db=mydb ERROR:  relation "nonexistent_table" does not exist
2024-11-14 08:00:05.901 UTC [12345]: [4-1] user=postgres db=mydb LOG:  statement: BEGIN;
2024-11-14 08:00:06.234 UTC [12345]: [4-2] user=postgres db=mydb LOG:  statement: COMMIT;
2024-11-14 08:00:07.567 UTC [12345]: [5-1] LOG:  autovacuum process started
```
2) В файле postgres.log найти записи, относящиеся к БД app
3) В файле postgres.log найти записи, содержащие error и вывести для них user и db
4) В директории text_processing создать файл nginx.conf с содержимым
```
user www-data;
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    upstream backend {
        server 10.0.0.1;  
        server 10.0.0.2;  
        server 10.0.0.3; 
        # server 10.0.0.1 weight=3; 
        # server 10.0.0.2 max_fails=2 fail_timeout=30s;
    }
    server {
        listen 80; 
        server_name example.com;

        location / {
            proxy_pass http://backend;  
            proxy_set_header Host $host; 
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```
5) В файле nginx.conf найти server_name и вывести только его значение
6) В файле nginx.conf найти все активные upstream (активный, значит в строке перед server не стоит знак #)
7) В файле nginx.conf найти все header и вывести их значения
8) В директории text_processing создать файл php-fpm.conf с содержимым
```
;;;;;;;;;;;;;;;;;;;;;
; FPM Configuration ;
;;;;;;;;;;;;;;;;;;;;;

; Global Options
[global]

pid = /run/php/php-fpm.pid

error_log = /var/log/php-fpm.log

log_level = notice

daemonize = yes

; syslog.facility = daemon
; syslog.ident = php-fpm

rlimit_files = 1024

;;;;;;;;;;;;;;;;;;
; Pool Definitions ;
;;;;;;;;;;;;;;;;;;

[www]

user = www-data
group = www-data

listen = /var/run/php/php-fpm.sock

listen.owner = www-data
listen.group = www-data
listen.mode = 0660

pm = dynamic
pm.max_children = 50
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 10
pm.process_idle_timeout = 10s;

pm.max_requests = 500

php_admin_value[error_log] = /var/log/php-fpm/www-error.log
php_admin_flag[log_errors] = on

php_value[memory_limit] = 128M
php_value[max_execution_time] = 30

php_admin_value[disable_functions] = exec,passthru,shell_exec,system
```
9) В файле php-fpm.conf найти пользователя и группу
10) В файле php-fpm.conf найти значение listen
11) В файле php-fpm.conf найти куда пишется error_log
# Часть 3
1) В домашней директории создать папку confs
2) Скопировать из директории text_processing файлы php-fpm.conf и nginx.conf в confs
3) Проверить с помощь grep и файла /etc/passwd, существуют ли пользователи www-data и php-fpm, если нет, то создать их
4) Сделать владельцем файла php-fpm.conf пользователя php-fpm, а группой владельцев - www-data
5) Сделать владельцем файла nginx.conf пользователя www-data, а группой владельцев - php-fpm
6) Создать пользователя devops
7) Добавить пользователя devops в группы php-fpm и www-data
8) Получить из файлов /etc/passwd и /etc/group информацию о добавленном пользователе (его id и в каких группах он состоит)
9) В директории confs создать директорию redis
10) В директории redis создать файл redis.conf
11) Посмотреть режим доступа на файл redis.conf
12) Добавить всем пользователям бит x на файл redis.conf
13) Убрать бит x у всех пользователей на файл redis.conf
14) В директории confs создать файл env
15) Установить права доступа так, чтобы только владелец мог читать и записывать в него, а остальные пользователи не имели никакого доступа
16) Установить права на файл redis.conf так, чтобы владелец имел полные права (чтение, запись, выполнение), группа могла только читать, а остальные пользователи не имели доступа
17) В директории confs создать файл inv
18) Установить права на файл inv так, чтобы владелец мог читать и записывать, группа могла читать и записывать, а остальные пользователи не имели доступа
19) В директории confs создать директорию private
20) Установить права на директорию private так, чтобы только владелец может читать и записывать файлы, а остальные пользователи не имеют прав
