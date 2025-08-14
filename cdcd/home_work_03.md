### I. python-docker-app
1) Создать директорию `python-app` и в ней создать файлы
- app.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Python!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```
- requirements.txt
```txt
Flask
```
- Dockerfile
- Jenkinsfile

2) Запустить приложение в docker
3) В github создать репозиторий python-docker-app и запушить в него созданную директорию
4) Написать Jenkinsfile для деплоя этого приложения в docker

### II. java-docker-app
1) Создать директорию `java-app` и в ней иницилизировать следующую структуру
```text
java-app/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── example/
│                   └── DemoApplication.java
├── pom.xml
├── Dockerfile
└── Jenkinsfile
```
- DemoApplication.java
```java
package com.example;
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@RestController
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @RequestMapping("/")
    String hello() {
        return "Hello World from Java!";
    }
}
```
- pom.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.0</version>
    </parent>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>
```
- Dockerfile
```dockerfile
FROM maven:3.8.6-openjdk-11 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn package -DskipTests

FROM openjdk:11-jre-slim
COPY --from=build /app/target/demo-0.0.1-SNAPSHOT.jar /app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```
2) В github создать репозиторий java-docker-app и запушить в него созданную директорию
3) Написать Jenkinsfile для деплоя этого приложения в docker
### III. ruby-docker-app
1) Инициализировать структуру
```text
ruby-app/
├── app.rb
├── Gemfile
├── Dockerfile
└── Jenkinsfile
```
- app.rb
```ruby
require 'sinatra'
set :port, 80
get '/' do
    'Hello World from Ruby!'
end
```
- Gemfile
```ruby
source 'https://rubygems.org'
gem 'sinatra'
gem 'puma'
```
- Dockerfile
```dockerfile
FROM ruby:3.1-alpine
WORKDIR /app
COPY Gemfile* .
RUN bundle install
COPY . .
ENTRYPOINT ["ruby", "app.rb"]
```
2) В github создать репозиторий ruby-docker-app и запушить в него созданную директорию
3) Написать Jenkinsfile для деплоя этого приложения в docker
