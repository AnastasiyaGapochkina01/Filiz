# Простое приложение
**У нас есть код на python, который надо запустить в docker**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/main")
def main():
    return "Hello admin"

@app.get("/admin")
def admin():
    return "Some admin actions here"
```
Запускам контейнер с `python:3.12` и работаем прямо в нем
```bash
docker run -d -it python:3.12
docker ps
docker exec -it fc0143ec6f27 bash
```

<img width="834" height="359" alt="image" src="https://github.com/user-attachments/assets/8641ab67-5af4-44a0-b2d9-a4c09f6a598b" />

Сразу установим себе текстовый редактор

<img width="615" height="59" alt="image" src="https://github.com/user-attachments/assets/9b354e7a-72c5-4cfc-af87-0d4a8f437b41" />

Создадим директорию для кода и перейдем туда

<img width="598" height="64" alt="image" src="https://github.com/user-attachments/assets/9f76a5ea-49e8-44d3-9e1d-519972f17da6" />

Создаем файл с кодом `main.py`

Как запустить? Первое что приходит в голову - `python3 main.py`. Пробуем

<img width="412" height="114" alt="image" src="https://github.com/user-attachments/assets/3f5bc499-d037-471b-809a-1a7b978a606f" />

Ругается. Ставим `fastapi`
```bash
pip install fastapi
```

Снова пробеум и теперь вроде отработало, но фактически ничего не запустилось

<img width="1433" height="302" alt="image" src="https://github.com/user-attachments/assets/9e70b90e-608b-4c6d-bb8d-ae2c980a01d6" />

Идем в гугл спрашивать как запустить fastapi

<img width="1440" height="327" alt="image" src="https://github.com/user-attachments/assets/0688c8f4-9d7d-49b1-9f0d-cd84bb9532ac" />

Там нам предлагают например так https://fastapi.tiangolo.com/deployment/manually/#run-a-server-manually

```bash
fastapi run main.py
```

И на нас опять ругаются

<img width="731" height="298" alt="image" src="https://github.com/user-attachments/assets/545e472a-e5b6-4be7-80ae-ec0c3da27aed" />

Ставим `fastapi[standard]` и пробуем еще раз и есть контакт, запустилось

<img width="1432" height="584" alt="image" src="https://github.com/user-attachments/assets/4eb1a634-4efd-4c3e-a8ea-2a432912d10a" />

Теперь это нужно конвертировать в `Dockerfile`

<img width="1440" height="360" alt="image" src="https://github.com/user-attachments/assets/3dcc5611-4a46-478b-8acb-02092b1f3650" />

Собираем и пробуем запускать
```bash
docker build -t fastapi-ex .
docker run -d -it -p 8000:8000 fastapi-ex
docker ps

curl 127.0.0.1:8000/main
curl 127.0.0.1:8000/admin
```

<img width="1424" height="660" alt="image" src="https://github.com/user-attachments/assets/cc1e0663-3271-4c9d-bd29-91085fbfc892" />

Победа 🏆

# Приложение с БД
**Нам дано некое приложение, например https://github.com/AnastasiyaGapochkina01/example-of-diploma. Необходимо запустить его в docker**
### Алгоритм действий
#### Клонируем репозиторий
```bash
git clone https://github.com/AnastasiyaGapochkina01/example-of-diploma.git
```
и переходим в директорию 
```bash
cd example-of-diploma
```

<img width="1197" height="225" alt="clone" src="https://github.com/user-attachments/assets/0ed64475-a9cf-4cd7-bf50-cb512fbfd4fd" />

#### Смотрим что есть в репозитории и определяемся с языком программирования
```bash
ls -l
```
У нас это python.
#### Запуск методом "в лоб"
У нас уже есть `Dockerfile`, значит мы можем собрать с его помощью image и попробовать его запустить
```bash
docker build -t diplom .
docker run -d -it diplom:latest
```

<img width="983" height="201" alt="image" src="https://github.com/user-attachments/assets/40c1807a-709b-4a31-ba5d-3c8067fb5f8f" />

И после сборки запустить. Он не запустился. Значит идем читать логи


```bash
docker logs f5a1121954e4
```

<img width="1432" height="563" alt="fail_1" src="https://github.com/user-attachments/assets/b0149c29-3fe1-46db-ad25-5a4b0876b44e" />


В логах видим ошибку

<img width="1023" height="135" alt="image" src="https://github.com/user-attachments/assets/011ad5e6-17e3-47ed-b517-1a01beb662b5" />

Идем в гугл читать

<img width="1440" height="477" alt="image" src="https://github.com/user-attachments/assets/72a68ace-58a1-44ba-a2c9-8aa80c1d8b70" />

Находим

<img width="685" height="659" alt="image" src="https://github.com/user-attachments/assets/b2ca7db6-e129-4706-8b26-c1f9420e42db" />

То есть наше приложение ищет `db`, но не находит его. И нам надо запустить контейнер с postgres.

> [!CAUTION]
> это отдельный контейнер. В image приложения кроме самого приложения и _библиотек/модулей_ ничего засовывать не надо

И там же нам дали пример compose. Заберем его, уберем порты (они базе не нужны в таком варианте) и добавим наше приложение

```yaml
services:
  db:
    image: postgres:16
    restart: always
    environment:
      POSTGRES_PASSWORD: pw1234
      POSTGRES_DB: base123

  diplom:
    image: diplom
    restart: always
    ports:
      - 8000:8000
```
> [!NOTE]  
> Из Dockerfile мы знаем что порт у приложения 8000; а image мы уже собрали и берем его

Запускаем
```bash
docker compose up -d
```

И вроде все даже неплохо выглядит

<img width="1423" height="423" alt="image" src="https://github.com/user-attachments/assets/fb020640-2f66-49f2-9235-c02b66192484" />


Проверяем

```bash
docker compose ps
```
И видим что наш контейнер с приложением рестартуется. Значит с ним что-то не так (мы прописали политику `restart: always`, а это значит что docker пытается перезапустить контейнер при _любой_ ошибке)

<img width="1433" height="127" alt="image" src="https://github.com/user-attachments/assets/fa18c4bb-cfef-42e6-8c4a-045469de3be9" />

Снова идем в логи

<img width="1439" height="214" alt="logs_2" src="https://github.com/user-attachments/assets/de4b7591-0367-4b75-bc91-7924aac7a114" />

И в самом конце находим

<img width="1440" height="87" alt="image" src="https://github.com/user-attachments/assets/15bfa1a5-efd9-4b9d-8e79-cd87a2ec5b4d" />

Идем в гугл (он тут будет тебе сложен, поэтому можно сразу в нейросетку)

Там он предложит варианты, нам пригодятся два

Первый это задать переменные приложению и базе

<img width="667" height="510" alt="v1" src="https://github.com/user-attachments/assets/eff0316e-f7d6-400e-ba48-9bd1505e340a" />

Если с postgres понятно, то вот у приложения имена переменных могут быть другие (например, не `DB_URL`, а как-то по другому). Ищем по папке с приложением что-то про переменные

```bash
grep -rE 'DB.*' ./
```

И находим 

<img width="913" height="409" alt="app" src="https://github.com/user-attachments/assets/c24f02ce-d9b5-4805-8b03-4f69b1764fac" />

Нейросетка примерно то же предполагала

<img width="646" height="386" alt="v2" src="https://github.com/user-attachments/assets/93f82900-a027-4f56-850a-4261e43a484d" />

Нам надо добавить правильные переменные для приложения и правильные значения для postgres

```yaml
services:
  db:
    image: postgres:16
    restart: always
    environment:
      POSTGRES_PASSWORD: secretpass123
      POSTGRES_DB: diplom
      POSTGRES_USER: appuser

  diplom:
    image: diplom
    restart: always
    ports:
      - 8000:8000
    environment:
      DB_USER: appuser
      DB_NAME: diplom
      DB_HOST: db
      DB_PASS: secretpass123
```

Перезапукаем все
```bash
docker compose down -v
docker compose up -d
docker compose ps
```

Запустилось

<img width="1424" height="328" alt="image" src="https://github.com/user-attachments/assets/d9a10098-e096-4ec3-8bbd-d11c6eed5185" />

Проверяем (запросы есть в `README.md`)

<img width="1324" height="118" alt="image" src="https://github.com/user-attachments/assets/295d8eaa-5e43-4ed2-9333-6cf1df94d5a3" />

Победа 🏆
