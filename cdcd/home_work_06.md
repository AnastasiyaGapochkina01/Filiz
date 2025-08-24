# Теория про GIT
1) Введение: https://youtu.be/0ZGPADQf29Q
2) Начало работы: https://youtu.be/-kegdnmqM5U
3) Подключение к GitHub: https://youtu.be/JuF57RoP-FU
4) Анализ измененеий: https://youtu.be/2w-q2Tbae0c
5) Файл .gitignore: https://youtu.be/Vrc3yAL1bzQ
6) Ветвление: https://youtu.be/F7KrpZCJT8Y

# Практика по GIT (+docker)
1) Создать _локальный_ репозиторий, создать в нем файл README.md с содержимым
```markdown
# Ecommerce API

```
Создать коммит с сообщением `Add readme`

2) Создать _удаленный (remote)_ репозиторий, подключить его к локальному репозиторию и запушить в него изменения
3) В _локальном_ репозитории создать ветку `feture-001`; изменить в этой ветке файл README.md, добавив в него текст (после первой строки)
```markdown
A simple API for managing online store products using Go, PostgreSQL, and Docker.
## Functions
- **CRUD for products:** create, read, update, delete
- **Metrics:** total number of goods, total stock balance, number of goods by category
- Containerization using Docker

## Endpoints

| Method | Path | Description |
|-------|------|----------|
| GET | `/products` | Get a list of all products |
| GET | `/products/{id}` | Get the product by ID |
| POST | `/products` | Create a new product |
| PUT | `/products/{id}` | Update an existing product |
| DELETE | `/products/{id}` | Delete an item |
| GET | `/metrics` | Get store metrics |

## Query examples
### Product creation
`bash
curl -X POST -H "Content type: application/json" -d '{
"name": "New product",
"price": 99.99,
"Description": "Best product",
"Quantity in stock": 10,
"category": "electronics"
}' http://localhost:8080/products
```
Закоммитить изменения

4) Добавить в репозиторий все файлы из репозитория https://github.com/AnastasiyaGapochkina01/golang-ecom; запустить приложение с помощью docker compose.
**К следующему заданию переходить только после того, как приложение заработало в docker**

5) Запушить ветку `feture-001` в `main` созданного выше репозитория
6) Создать Pull Request и смержить изменения в `main`
