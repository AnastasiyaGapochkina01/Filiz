Написать пайплайн для запуска различных этапов CI/CD через Jenkins pipeline на основе входных параметров для приложения
https://github.com/AnastasiyaGapochkina01/py-cicd-app

### Параметры пайплайна
- RUN_TEST (boolean) — запуск тестов (`--action test`).
- RUN_CHECK (boolean) — запуск healthcheck (`--action check`).
- RUN_BUILD (boolean) — запуск сборки (`--action build`).
- RUN_APPLY (boolean) — запуск применения к окружению (`--action apply`).
- ENV (choice) — выбор окружения для apply (dev, staging, prod).

### Логика пайплайна
Каждый этап запускается только если соответствующий boolean-параметр установлен в true.

Для выполнения каждого этапа запускается Python-скрипт с нужными параметрами.

Этап apply обязательно получает параметр ENV.
