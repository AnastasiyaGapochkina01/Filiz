Запустить с помощью systemd приложение из репозитория https://github.com/AnastasiyaGapochkina01/python-cmdb в соответствии с требованиями:
1) запуск приложения должен осуществляться от имени пользователя cmdbuser (добавить его в систему, если его не существует)
2) в unit-файле в секции Service добавить логирование
```bash
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=cmdb-service
```
3) в директории `/etc/rsyslog.d` создать файл `cmdb.conf` с содержимым
```bash
if $programname == 'cmdb-service' then /var/log/cmdb.log
& stop
```
создать пустой файл `/var/log/cmdb.log` и назначить владельца `syslog`, а группу `adm`; перезапустить службу rsyslog

