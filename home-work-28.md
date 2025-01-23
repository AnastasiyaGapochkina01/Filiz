# Часть 1
1) В директории text_processing создать файл rnd_office_worker с содержимым
```
Smirnova O.V. [SERVICE: development] +79123456789 G4
[SERVICE: management] Kuznetsov V.D. kuznetsovvd@gmail.com G5
Sokolov I.V. +79051234567 [SERVICE: security] G3
[SERVICE: development] Volkova N.D. volkovand@gmail.com G5
Novikov I.F. [SERVICE: accountant] +79196543210 novokovif@gmain.com G10
```
2) С помощью регулярных выражений и grep получить из файла rnd_office_worker
- все номера телефонов
- все email
- все подразделения (то, что в квадратных скобках)
- имена сотрудников и их грейды (грейд здесь -- последний столбец)
3) В директории text_processing создать файл msk_servers с содержимым
```
compute-1 192.168.3.2 NSK [roles: service]
192.168.3.3 compute-2 [roles: back] [app: bookshop] SPB
[roles: back] compute-3 [app: bookshop] MSK 192.168.3.4
compute-4 192.168.3.5 RND [role: front] [app: landing]
```
4) С помощью регулярных выражений и grep получить из файла msk_servers
- все ip-адреса
- все роли
- все app
- все локации

# Часть 2
1) В директории text_processing/process создать файл gen_log.sh
```
#!/bin/bash

generate_random_ip() {
    echo "$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
}

generate_http_method() {
    methods=("GET" "POST" "HEAD" "PUT" "DELETE")
    echo "${methods[$((RANDOM % ${#methods[@]}))]}"
}

generate_random_path() {
    paths=("/index.html" "/about" "/contact" "/products" "/blog")
    echo "${paths[$((RANDOM % ${#paths[@]}))]}"
}

generate_user_agent() {
    agents=(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "Mozilla/5.0 (X11; Linux x86_64)"
    )
    echo "${agents[$((RANDOM % ${#agents[@]}))]}"
}

while true; do
    ip=$(generate_random_ip)
    method=$(generate_http_method)
    path=$(generate_random_path)
    status_codes=("200" "404" "500" "403")
    status=${status_codes[$((RANDOM % ${#status_codes[@]}))]}
    bytes=$((RANDOM % 10000 + 100))
    user_agent=$(generate_user_agent)
    timestamp=$(date "+%d/%b/%Y:%H:%M:%S %z")

    log_entry="$ip - - [$timestamp] \"$method $path HTTP/1.1\" $status $bytes \"-\" \"$user_agent\""

    echo "$log_entry" >> from_script.log

    sleep 15
done
```
2) Сделать файл gen_log.sh исполняемым для всех
3) Выполнить команду ```./gen_log.sh &```
4) Проверить, появился ли в директории файл from_script.log
5) Найти с помощью ps процесс gen_log.sh и вывести для него ppid,pid,stat,comm
6) Приостановить процесс gen_log.sh; проверить как изменился столбец stat
7) Возобновить процесс gen_log.sh; проверить как изменился столбец stat
8) Убить процесс gen_log.sh
9) Вывести первые 5 строк из файла from_script.log
10) Из файла from_script.log получить все ip адреса (любым способом)
11) Из файла from_script.log получить все методы (любым способом)
12) Из файла from_script.log получить все коды ответа (любым способом)
13) Из файла from_script.log получить все URI

<img width="891" alt="image" src="https://github.com/user-attachments/assets/34aaa08d-8801-44ca-bfde-8cbbedc13dda" />
