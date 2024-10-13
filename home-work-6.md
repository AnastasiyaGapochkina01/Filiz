# Часть 1
1) Отфильровать вывод команды lscpu так, чтобы получить значение CPU MHz
2) Отфильровать вывод команды lscpu так, чтобы получить значение Hypervisor vendor
3) Из файла /proc/meminfo получить все строки. относящиеся к HugePages
4) Отфильтровать вывод команды lsblk так, чтобы получить все разделы (раздел это та строка, где 6 поле имеет значение part)
5) Для полученных в предыдущем задании разделов вывести их имена
6) С помощью awk вывести из файла /etc/passwd имена всех пользователей (первое поле)
7) С помощью awk вывести из файла /etc/passwd последнее поле
8) Отфильтровать вывод команды free -h так, чтобы получить размер Swap
9) Из файла text_processing/products (создавали в прошллой домашке) с помощью awk вывести все строки, содержащие слово PROD-C
10) Из файла text_processing/products (создавали в прошллой домашке) с помощью awk вывести все строки, содержащие слово product-3 и вывести для них последний столбец

# Часть 2
1) В директории home_works создать директорию app. *!! Дальнейшие действия выполнять не уходя из директории home_works !!*
2) В директории app создать файл main.go с содержимым
```
package main

import (
"fmt"
"log"
"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.URL.RawQuery)
	fmt.Fprintf(w, `
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
Hello from Docker!

`)
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```
3) В директории app создать директорию docker
4) В директории docker создать файл Dockerfile с содержимым
```
FROM golang:1.22 AS builder
WORKDIR /go/src/app
COPY main.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /go/bin/web_server main.go

FROM alpine
COPY --from=builder /go/bin/web_server .
ENTRYPOINT ["/web_server"]
```
5) В директории app создать директорию data
6) В директории data создать директории golang и mysql
7) В директории app создать файл compose.yaml
8) Переименовать директорию app в golang_app (```mv app golang_app```)
9) Содать директорию applications
10) Переместить golang_app в applications (```mv golang_app  applications```)
