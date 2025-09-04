FROM golang:1.23
WORKDIR /app
COPY . .

RUN go mod init sitechecker
RUN go mod tidy
RUN go build -o site-checker
ENTRYPOINT ["/app/site-checker"]