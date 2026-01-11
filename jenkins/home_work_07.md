1) Установить на машину с Jenkins golang (инструкция тут https://go.dev/doc/install)
2) Написать pipeline для приложения https://github.com/AnastasiyaGapochkina01/go-app-cicd; **требования к pipeline**:
- при запуске доступны параметры
  - RUN_TESTS (booleanParam - запускать ли тесты, значение по умолчанию: true)
  - IMAGE_TAG (string - название docker image)
  - BRANCH (gitParameter - из какой ветки репозитория собирать)
- пайплайн состоит из этапов
  - клонирование репозитория
  - прогон тестов (перейти в директорию с проектом и выполнить `go test ./`) - только если отмечен чекбокс RUN_TESTS
  - сборка docker image с именем, заданным в IMAGE_TAG
