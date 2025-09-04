# Сбор общих сведений о проекте/репозитории
Что выяснили из `README.md`
1) Это веб-сервис. а значит будет порт. Какой порт? Смотрим в код, так как в `README.md` нет никаких данных про это. Ищем что-то в духе `listen` или `host` [Находим тут](https://github.com/AnastasiyaGapochkina01/dos-29-diplomas-projects/blob/vkuchumov/sitechecker/main.go#L182) `Listening on :8080`. Это будет _внутренний_ порт. Внешний - выбираем самостоятельно.
2) В `README.md` указан Go как язык разработки, а значить docker image будет собираться на основе image golang. Нет указания версии, поэтому можно будет взять не слишком старую, но и не самую последнюю (на момент написания этого файла самая новая - 1.25), возьмем 1.23
3) Так же в `README.md` указана база данных postgresql
4) Теперь надо проверить, какие переменные использует (и использует ли вообще) приложение. В main.go видим такой [блок для подключения к БД](https://github.com/AnastasiyaGapochkina01/dos-29-diplomas-projects/blob/vkuchumov/sitechecker/main.go#L31-L37). Для поиска можно воспользоваться грепом (не забыть перейти в папку с проектом)
```bash
grep -EIRi "(env|getenv)" ./
```
Увидим
```
./main.go:      os.Getenv("PGUSER"),
./main.go:      os.Getenv("PGPASSWORD"),
./main.go:      os.Getenv("PGHOST"),
./main.go:      os.Getenv("PGPORT"),
./main.go:      os.Getenv("PGDATABASE"),
./main.go:      os.Getenv("PGSSLMODE"),
```
Это те переменные, которые использует **приложение**

---

# План работ
1) Склонировать репозиторий
2) Написать Dockerfile
```dockerfile
FROM golang:1.23
...
````
3) Собрать image 
```bash
docker build -t site-checker ./
docker image ls
```
4) Написать compose файл, состоящий из двух сервисов
- appliaction
- postgres
5) Запустить приложение
```bash
docker compose up -d
docker compose ps -a
```
Вывод `docker compose ps` смотреть внимательно, если какой-то контейнер постоянно попадает в статус 'Restarting' - он не работает. В этом случае делаем 
```bash
docker compose logs $service_name
```
где `$service_name` это _имя сервиса_ в compose файле
6) Проверить. Проверки определяются либо в `README.md` - чаще всего это запросы `curl`; либо на основе функциональности приложения. В нашем случае:
- должен быть UI на 127.0.0.01:8080 с формой
- через форму добавляется сайт
- наличие дашбордов