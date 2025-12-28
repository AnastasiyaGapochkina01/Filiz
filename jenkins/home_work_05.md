Написать Jenkins пайплайн для приложения https://github.com/AnastasiyaGapochkina01/http-py/tree/main
# Требования
1) При запуске доступны параметры
- `RUN_TESTS` booleanParam (чек-бокс) - запускать ли тесты (значение по умолчанию - true)
- `APP_VERSION` string (строка) - версия релиза (значение по умолчанию - latest)
- `TARGET` choices (выпадающий список) - целевое окружение для деплоя (варианты: `s3`, `docker-server`, `bare-metal`)
- `BRANCH` gitParameter - ветка репозитория для деплоя
2) Сам пайплайн состоит из этапов
- проверка кода линтером (`stage('Linter')`)
- сборка релиза (`stage('Build')`) - как собирать приложение описано в его README
- запуск тестов (`stage('Tests')`) - запуск тестов (если отмечен `RUN_TESTS`); как запускать тесты
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pytest
pytest server.py
```
- создание архива с релизом
```bash
tar -czf http-server-${APP_VERSION}.tar.gz dist/server
```
где `APP_VERSION` это параметр из п1
- оповещение (`stage('Finish')`) - вывод с помощью echo сообщения `CI process success`
