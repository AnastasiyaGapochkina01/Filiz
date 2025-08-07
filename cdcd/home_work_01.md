1) Запустить Jenkins
2) Создать минимальный pipeline с 2 stage (build и deploy), который
- использует любой доступный агент
- в stage build выводит сообщение `Running build stage...`
- в stage deploy выводит сообщение `Deploy on server started...`
3) Создать pipeline, который:
- определяет переменную окружения DEPLOY_ENV со значением "production"
- выводит значение переменной в stage config
