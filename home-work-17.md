# Часть 1: Работа с процесами
1) Вывести список всех процессов
2) В списке процессов с помощью grep найти процесс bash
3) Для найденного процесса bash вывести только id, user и comm
4) Выполнить команду
```
sleep 15000 &
```
5) В списке процессов с помощью grep найти процесс sleep
6) Остановить процесс sleep

# Часть 2: Пользователи и права доступа
1) Удалить пользователей ansible, grafana, prometheus и cadvisor, postgres-exporter и node-exporter
2) Создать пользователей terraform, admin
3) Создать группу infra и добавить в нее пользователей terraform, admin
4) В директории /opt создать директорию infrastructure
5) Установить для директории /opt/infrastructure  права доступа так, чтобы группа infra имела к ней полный доступ
6) В директории text_processing создать файл all_tasks и сделать его владельцем пользователя admin
7) В директории /opt/infrastructure создать директории tf, provision
8) В директории provision создать директорию roles и файл setup.yaml
9) В директории tf создать файлы main.tf, disks.tf, meta.txt
10) Назначить владельцем директории tf пользователя terraform, а группой - infra
11) Сделать terraform владельцем и группой владельцев файлов main.tf, disks.tf, meta.txt
12) Создать нового пользователя (с произвольным именем) без домашней директории и без возможности входа в систему (задача со "звездочкой")

# Часть 3: Обработка текста
1) С помощью ls и grep найти в директории text_processing все файлы с расширением .log
2) Выполнить команду ```curl -s https://jsonplaceholder.typicode.com/todos/1``` и из ее вывода получить только значение поля title
3) Вывести список процессов, запущенных от имени vboxuser
4) В директории text_processing создать файл conf.ini с содержимым
```
[General]
AppName = MyAwesomeApp
Version = 1.0.3
Language = ru_RU
Debug = false
SMTPServer = smtp.example.com

#[Network]
#ServerAddress = 192.168.1.100
#ServerPort = 8080
#Timeout = 30

[Database]
Host = localhost
Port = 5432
Name = myapp_db
User = db_user
Password = s3cr3t_p@ssw0rd
```
5) Выведите содержимое файла conf.ini, исключив все строки комментариев (начинающиеся с #)
6) Из файла conf.ini получить значение Language и SMTPServer
7) Выяснить, существует ли в директории /etc/ файл resolv.conf, если да, то получить из него значение domain
8) Выяснить, существует ли в директории /etc файл ntp.conf, если да, то вывести его содержимое , исключив все строки комментариев (начинающиеся с #) и найти строки начинающиеся с pool
9) В директории text_processing создать файл contacts.txt с содержимым
```
# Contacts
Name,Last Name,Email,Phone
Ivan,Ivanov,ivan.ivanov@example.com,+7-123-456-7890
Maria,Petrova,maria.petrova@example.com,+7-234-567-8901
Alex,Sidorov,alexey.sidorov@example.com,+7-345-678-9012
Elena,Kuznetsove,elena.kuznetsova@example.com,+7-456-789-0123

# Additional contacts
Petr, Semenov,petr.semenov@example.com,+7-135-246-3579
Roman,Kovalev,roman.kovalev@example.com,+7-357-468-5791
```
10) В файле contacts.txt найти все e-mail
11) В файле /proc/cpuinfo найти количество ядер CPU (CPU(s))
12) В директории text_processing создать файл webpage.html с содержимым
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример веб-страницы</title>
</head>
<body>
    <div class="container">
        <h1>Добро пожаловать на пример веб-страницы</h1>
        <p>Эта страница содержит различные элементы HTML и ссылки для демонстрационных целей.</p>
        
        <h2>Полезные ссылки:</h2>
        <ul class="link-list">
            <li><a href="https://www.example.com">Пример.com</a></li>
            <li><a href="https://www.google.com">Google</a></li>
            <li><a href="https://www.github.com">GitHub</a></li>
            <li><a href="https://www.stackoverflow.com">Stack Overflow</a></li>
        </ul>

        <h2>Изображение:</h2>
        <img src="https://via.placeholder.com/300x200" alt="Пример изображения">

        <h2>Контактная информация:</h2>
        <p>Email: <a href="mailto:info@example.com">info@example.com</a></p>
        <p>Телефон: <a href="tel:+71234567890">+7 (123) 456-78-90</a></p>

        <h2>Дополнительные ресурсы:</h2>
        <ul>
            <li><a href="https://www.w3schools.com">W3Schools</a> - учебные материалы по веб-разработке</li>
            <li><a href="https://developer.mozilla.org">MDN Web Docs</a> - документация для веб-разработчиков</li>
        </ul>
    </div>
</body>
</html>
```
13) В файле webpage.html найти все ссылки
