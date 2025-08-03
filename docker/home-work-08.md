Дано приложение-блог, состоящее из
- backend: https://gitlab.com/devops201206/dh-blog-backend#
- frontend: https://gitlab.com/devops201206/dh-blog-frontend#

Необходимо
1) Запустить backend в docker
2) Настроить nginx на хосте так, чтобы он раздавал файлы frontend с диска (из директории `/var/www/dh-frontend`) и проксировал на backend
3) Запустить два экземпляра backend и донастроить nginx так, чтобы он балансировал запросы между двумя экземплярами
