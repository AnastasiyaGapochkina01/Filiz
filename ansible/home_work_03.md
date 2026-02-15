1) Написать плейбук, который клонирует репозиторий https://github.com/AnastasiyaGapochkina01/it-profs.git в `/opt/repos`
2) Написать плейбук, который
- создает `/opt/backups/configs`
- копирует `/etc/ssh/sshd_config` в `/opt/backups/configs/sshd_config.bak`
3) Написать плейбук, который:
- создает пользователя `appuser`, с домашней директорией `/opt/test-app`
- создает файл `/opt/test-app/app.py` с содержимым `print("Hello Ansible!")`
- создает `.env` файл с содержимым `APP_PORT=3000`
- делает владельцем директории `/opt/test-app` пользовтаеля `appuser`
4) Написать плейбук, который:
- создает файл `/var/www/html/index.html` с содержимым  `<h1>Demo Site on {{ ansible_fqdn }}</h1>`
- устанавливает nginx (если еще не установлен)
- делает проверку сайта с помощью `curl`
5) Написать плейбук для установки MariaDB
