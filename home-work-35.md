1) Написать скрипт, который будет принимать на вход имя пользователя и проверять, существует ли такой в системе. Если существует, то скрипт должен вывести
- имя пользователя
- UID
- shell
в формате
```
User $user_name exist on $hostname with ID $user_id and command shell $user_shell

user anestesia exist on swarm-master with ID 1000 and command shell /bin/zsh
```
Если пользователя не существует, то вывести
```
User $user_name not exist
```
2) Написать скрипт, который будет принимать на вход имя пользователя и проверять, состоит ли он в группе sudo. Если да, то выводить на экран
```
$user_name is privileged

anestesia is privileged
```
если нет, то выводить на экран
```
$user_name is not privileged

student is not privileged
```
3) Написать скрипт, который будет на вход принимать путь к директории и собирать о ней следующую статистику
- владелец директории
- сколько в ней файлов
Результат вывести на экран в формате
```
Owner of $dir_name is $owner and it has $files_count files

Owner of /home/anestesia/ansible is anestesia and it has 2 files
```
4) Написать скрипт, который будет имитировать заметки: при запуске скрипта он должен спрашивать пользователя "what do you want to note?",
считывать пользовательский ввод и записывать его в файл notes.txt в формате
```
---
$date_time $user_note
---

---
2025-44-20 07:03 training with a dog handler today
---
```
5) Написать скрипт, который будет принимать на вход дату и время в формате ```YYYY-MM-DD HH:mm```  и искать в файле notes.txt (который мы создали в предыдущем скрипте) записи за эту дату
