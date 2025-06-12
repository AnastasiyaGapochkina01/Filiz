# Часть 1
1) Создать директорию `/var/www/bash-apps`
2) В директории `/var/www/bash-apps` создать файл `hello.sh` с содержимым
```
#!/bin/bash
while true; do
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] Hello from systemd!" >> /var/log/hello_world.log
  sleep 5
done
```
3) Сделать файл `hello.sh` исполняемым
4) Написать systemd-unit для запуска скрипта `hello.sh`; запустить написанную службу
5) Найти ID процесса, который запустился с помощью systemd-юнита
6) Убить найденный процесс и проверить, как ведет себя unit
# Часть 2
1) В директории `/var/www/bash-apps` создать файл `sys-monitor.sh` с содержимым
```
#!/bin/bash
# /usr/local/bin/resource_monitor.sh
LOG_DIR="/var/log/resource_monitor"
mkdir -p $LOG_DIR

while true; do
  TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')
  echo "--- Resource snapshot $TIMESTAMP ---" >> $LOG_DIR/metrics.log
  free -m >> $LOG_DIR/metrics.log
  df -h >> $LOG_DIR/metrics.log
  echo "-----------------------------------" >> $LOG_DIR/metrics.log
  sleep 60
done
```
2) Сделать файл `sys-monitor.sh` исполняемым
3) Написать systemd-unit для запуска скрипта `sys-monitor.sh`; запустить написанную службу
4) Найти ID процесса, который запустился с помощью systemd-юнита
5) Проверить, существует ли директория `/var/log/resource_monitor` и есть ли в ней файл `metrics.log`; если да, то посмотреть его содержимое
6) Убить найденный процесс и проверить, как ведет себя unit
