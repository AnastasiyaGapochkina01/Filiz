1) Создать в github репозиторий `jenkins-jobs`
2) Склонировать пустой репозиторий `jenkins-jobs` на ВМ с jenkins
3) Создать в локальном репозитории папку `simple-pipelines`
4) В `simple-pipelines` создать файл `Jenkinsfile-info-app`, который будет описывать пайплайн со следующей логикой
- при запуске доступны параметры
  - build: booleanParam (чек-бокс) - собирать ли новую версию приложения
  - release: строка, значение по умолчанию - latest, версия релиза
  - run release: booleanParam (чек-бокс) - осуществлять ли деплой
  - env: выпадающий список - целевой сервер для деплоя приложения (варианты: demo, prod)
  - branch: ветка репозитория для деплоя
- сам пайплайн состоит из этапов
  - сборка версии приложения (https://github.com/AnastasiyaGapochkina01/info-app)
  - тестирование собранной версии
  - деплой новой версии на целевое окружение (только если отмечен чек-бокс run release)
 
Моя реализация
https://github.com/AnastasiyaGapochkina01/jenkins-jobs/blob/main/simple-pipelines/Jenkinsfile-info-app
