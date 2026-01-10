Написать Jenkins пайплайн для приложения https://github.com/AnastasiyaGapochkina01/it-profs/tree/main
# Требования
1) При запуске доступны параметры
- `APP_VERSION` string (строка) - версия релиза (значение по умолчанию - latest)
- `TARGET` choices (выпадающий список) - целевое окружение для деплоя (варианты: `s3`, `docker-server`, `bare-metal`)
- `BRANCH` gitParameter - ветка репозитория для деплоя
2) Сам пайплайн состоит из этапов
- проверка кода и приложения и Dockerfile линтером
- сборка релиза - собрать docker image (Dockerfile есть в репозитории)
