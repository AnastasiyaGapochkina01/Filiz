# Часть 1
1) Установить docker
2) Проверить установку
```bash
docker --version
sudo docker run hello-world
```
3) Запустить контейнер с ubuntu и именем my-ubuntu
```bash
sudo docker run -it -d --name my-ubuntu ubuntu bash
```
Зайти в контейнер 
```bash
sudo docker exec -it my-ubuntu bash
```
Внутри контейнера установить nano и проверить его работу, создав в директории /opt файл hello с содержимым
```txt
Hello from Ubuntu container
```
выйти из контейнера
```bash
exit
```
4) Остановить контейнер
```bash
sudo docker stop my-ubuntu
```
5) Проверить через
```bash
sudo docker ps
sudo docker ps -a
```
6) Запустить контейнер
```bash
sudo docker start my-ubuntu
```
7) Остановить и удалить контейнер
```bash
sudo docker stop my-ubuntu
sudo docker rm my-ubuntu
```
# Часть 2
1) Запустить контейнер с debian и именем my-debian
2) Зайти в контейнер my-debian и внутри контейнера установить пакет procps; выйти из контейнера
3) Остановить контейнер my-debian
4) Запустить контейнер my-debian
5) Остановить и удалить контейнер my-debian
