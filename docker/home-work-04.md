1) Запустить в docker приложение
- app.py
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Docker and FastAPI!"}
```
- requirements.txt
```txt
fastapi
uvicorn
```
```
uvicorn main:app --host 0.0.0.0 --port 80
```
Проверка
```bash
curl 127.0.0.1:8080
{"message":"Hello, Docker and FastAPI!"}
```
2) Запустить в docker приложение
- index.php
```php
<?php
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'Неизвестно';
$date = date('d.m.Y H:i');
$name = $_POST['name'] ?? '';

echo "<h1>Hello, Docker and PHP!</h1>";
echo "<p>Сейчас: <strong>$date</strong></p>";
echo "<p>Ваш браузер: <strong>$userAgent</strong></p>";

echo '<form method="POST">
    <label>Ваше имя: <input name="name" /></label>
    <button type="submit">Отправить</button>
</form>';

if ($name) {
    echo "<p>Привет, <strong>" . htmlspecialchars($name) . "</strong>!</p>";
}
```
3) Запустить в docker приложение
- main.go
```golang
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, Docker and Go!")
    })
    fmt.Println("Сервер запущен на порту :8080")
    http.ListenAndServe(":8080", nil)
}
```
