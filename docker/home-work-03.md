Необходимо собрать docker image для приложения https://gitlab.com/devops201206/geo-data#

> [!IMPORTANT] 
> **Несмотря на то, что приложение многокомпонентное, его надо собирать в одном Dockerfile, так как по сути запускается напрямую там только `processor.py`. В качестве базового image взять `python:3.11-bookworm`**

Запустить из собранного image контейнер с именем `geo-data-1` и маппингом портов `8080:8080`. Проверка
```bash
curl 127.0.0.1:8080
```
Если отдается такое, то все ОК
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geo Distance Calculator</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
```
