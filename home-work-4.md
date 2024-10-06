# Часть 1: Повторение
1) В директории home_works создать директорию films
2) В директории films создать директории western, action, drama, comedy
3) Перейти в директорию western
4) Не выходя из директории western создать в директории action файлы JohnWick, Gentlemen и директорию FastFurious
5) Не выходя из директории western создать в директории drama файлы Intouchables, TheGreenMile, Hachi
6) Перейти в директорию films
7) В директории comedy создать директории movies и TVseries
8) В директории movies создать файлы HomeAlone, TheMask
9) В директории TVseries создать файлы Friends, MiracleWorkers, TheOffice
10) В директории home_works создать директорию films_archive
11) Скопировать *содержимое* директории films в films_archive
12) Переименовать директорию films_archive/western в films_archive/westernCopy
# Часть 2: Работа с текстом
1) В директории home_works создать директорию text_processing и перейти в нее
2) Создать файл info.csv с таким содержимым
```
Name:Company:Price:Ganre:Multiplayer
Item1:Company1:60000$:Ganre1:Yes
Item2:Company2:70000$:Ganre2:Yes
Item3:Company3:90000$:Ganre1:Yes
Item4:Company4:90000$:Ganre1:No
Item5:Company5:110000$:Ganre1:Yes
Item6:Company6:410000$:Ganre2:Yes
Item7:Company1:60000$:Ganre1:Yes
Item8:Company4:40000$:Ganre2:No
Item9:Company3:90000$:Ganre1:Yes
```
3) В файле info.csv с помощью grep найти строки, которые содержат слово No
4) В файле info.csv найти все строки, в которых встречается слово Ganre2
5) В файле info.csv найти все строки, в которых встречается слово Ganre2 и вывести только 3 поле
6) Создать файл metrics с содержимым
```
metric_name:metric_type:interval
cache_disk_use:gauge:1
cache_use:gauge:0
key_buffer_bytes_used:byte:3
table.rows.read:count:10
disk_use:gauge:10
data_size:gauge:1
rows_deleted:count:1
bytes_received:byte:1
```
7) В файле metrics найти все строки, в которых встречается слово gauge и вывести только первое поле
8) В файле metrics найти все строки, в которых встречается слово byte и вывести только 3 поле
9) В файле metrics найти все строки, в которых встречается слово disk и вывести только 2 поле
10) В файле metrics найти все строки, которые *начинаются* с cache
11) В файле info.csv найти все строки, которые содержат слово Company4
