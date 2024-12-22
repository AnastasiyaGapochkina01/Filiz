# Часть 1: Работа с текстом
1) В директории text_processing создать файл main-rabbitmq.conf с содержимым
```
listeners.tcp.default = 5672
management.tcp.port = 15672

loopback_users = none
default_vhost = /
default_user = guest
default_pass = guest

cluster_formation.peer_discovery_backend = rabbit_peer_discovery_classic_config
cluster_formation.classic_config.nodes.1 = rabbit@node1.example.com
cluster_formation.classic_config.nodes.2 = rabbit@node2.example.com
cluster_formation.classic_config.nodes.3 = rabbit@node3.example.com

queue_master_locator = min-masters

management.load_definitions = /etc/rabbitmq/definitions.json
```
2) Из файла main-rabbitmq.conf получить значения listeners.tcp.default и management.tcp.port
3) Вывести последнюю строку файла main-rabbitmq.conf
4) Из файла main-rabbitmq.conf вывести все строки, начинающиеся с ```default_```
5) Из файла main-rabbitmq.conf получить значения default_user и default_pass
6) В директории text_processing создать файл main-kafka.conf с содержимым
```
broker.id=0

listeners=PLAINTEXT://localhost:9092

log.dirs=/var/lib/kafka/data

zookeeper.connect=localhost:2181

num.partitions=3

default.replication.factor=1

log.retention.hours=168
log.segment.bytes=1073741824

```
7) Из файла main-kafka.conf получить значение log.dirs. Проверить, существует ли такая директория
8) Из файла main-kafka.conf вывести все строки, начинающиеся с ```log```
9) Из файла main-kafka.conf получить порт подключения к zookeeper
10) Проверить, существует ли директория /etc/perl/Net. Если да, то проверить, есть ли в ней файл libnet.cfg. Если да, то 
- вывести на экран его содержимое без строк, начинающихся с #
- найти в нем все строки, содержащие ftp
11) Выполнить команду ```file /dev/stderr```. Изучить вывод. Что такое /dev/stderr?
# Часть 2: Процессы
1) В домашней директории создать файл busyport.sh с содержимым
```
#!/bin/bash

find_and_listen_port() {
    for port in {8080..9090}
    do
        if ! netstat -tuln | grep -q ":$port "; then
            echo "Найден свободный порт: $port" >> busyport.log
            nc -l $port
            break
        fi
    done
}

find_and_listen_port
```
2) Сделать файл busyport.sh исполняемым для всех
3) Выполнить команду ```./busyport.sh > /dev/null &```
4) Найти процессс busyport в выводе команды ps
5) В директории /proc найти директорию, которая соответствует id процесса busyport
6) В найденной в предыдущем пункте директории найти файл stat и вывести из него первые три столбца
7) Проверить, появился ли в домашней директории файл busyport.log. Если да, то вывести его содержимое на экран. Какой порт там записан?
8) Выполнить команду sudo ss -nlp и в ее выводе найти порт из задания 7. Затем вывести для найденной строки только второе и пятое поля
9) Запустить htop и найти в нем процесс busyport
10) Убить процесс busyport
# Часть 3: Пользователи и права доступа
1) В домашней директории создать файл secret.txt и установить такие права доступа, чтобы только владелец мог читать и изменять его, а все остальные не имели никаких прав
2) В домашней директории создать директорию shared и настроить права так, чтобы владелец и группа могли читать, записывать и входить в нее, а остальные пользователи могли только входить и читать содержимое
3) Изменить права на файл busyport.sh так, чтобы владелец мог читать и выполнять его, группа могла только читать, а остальные не имели никаких прав.
4) В домашней директории создайть файл "readonly.txt" и установить права так, чтобы все пользователи могли его читать, но никто не мог изменять, включая владельца.
5) В домашней директории создать директорию team_project и настроить права так чтобы только группа имела полные права, а остальные (включая владельца) не могли ничего
6) В домашней директории создать файл public_info.txt и настроить права так, чтобы у всех был полный доступ к этому файлу
7) Проверить, существуют ли пользователи apple и rapsberry. Если нет - создать их
8) Изменить домашнюю директорию пользователя rapsberry на /home/pi-home
9) Задать пользователям apple и rapsberry пароли
10) Создать группу autstuff и добавить в нее apple и rapsberry
11) В директории /tmp создать две директории apple-data и pi-data, назначить владельцем директории apple-data пользователя apple, а директории pi-data - rapsberry
12) Назначить права на директории apple-data и pi-data так, чтобы
- у владельцев были полные права
- у группы - полные права
- у всех остальных никаких прав
13) Переключиться на пользователя apple
14) Попробовать создать файлы в директориях apple-data и pi-data, какие права у созданных файлов? Вернуться под обычного пользователя
