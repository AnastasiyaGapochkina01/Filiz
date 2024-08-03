# Часть 1
1) Удалить директорию lab01
2) Создать директорию lab_1
3) В lab_1 создать директорию storage
4) В директории storage создать каталог foodstuff
5) В директории storage создать каталог household_chemicals
6) В директории storage создать каталог toys
7) Перейти в каталог foodstuff
8) Создать в foodstuff директории fruits, groceries, milk_products
9) Не выходя из foodstuff содать в storage/household_chemicals директории cosmetic, laundry_products, cleaning_products
10) Не выходя из foodstuff содать в storage/toys директории educational_toys, soft_toys
11) Перейти в каталог foodstuff
12) В директории storage/foodstuff/fruits создать файл с именем apples и содержимым
```
Golden
Gala
Caramel
Fuji
Red
```
13) В директории storage/household_chemicals/cleaning_products создать файл с именем floor_products и содержимым
```
Mr Proper
Grass
Synergetic
```
14) В директории storage/household_chemicals/laundry_products создать файл с именем powders и содержимым
```
Persil
Laska
Tide
Ariel
```
15) Перейти в директорию storage/household_chemicals/cleaning_products
16 Не выходя из storage/household_chemicals/cleaning_products создать в storage/household_chemicals/cosmetic файл с именем lipsticks и содержимым
```
Beloris
Luxvisage
Novo Small
```
17) Не выходя из storage/household_chemicals/cleaning_products создать в storage/toys/educational_toys файл с именем constructors и содержимым
```
Arduino
Lego
```
18) Не выходя из storage/household_chemicals/cleaning_products создать в storage/toys/soft_toys файл с именем all_products и содержимым
```
Bear
Gouse
Lion
Tiger
```
18) Перейти в директорию storage/toys/soft_toys
19) Не выходя из storage/toys/soft_toys скопировать файл с именем all_products в storage/toys/
20) Не выходя из storage/toys/soft_toys создать РЯДОМ с директорией storage директорию shipment
21) Не выходя из storage/toys/soft_toys скопировать файл storage/foodstuff/fruits/apples в директорию shipment
22) Не выходя из storage/toys/soft_toys скопировать файл storage/household_chemicals/cleaning_products/floor_products в директорию shipment
23) Скопировать директорию storage/toys/ в директорию shipment
24) Скопировать содержимое storage/household_chemicals/ в директорию shipment
25) Выполнить команды tree -a shipment и tree -a storage
# Часть 2
1) Создать в домашней директории папку home_works
2) В home_works создать директорию seaport
3) В директории seaport создать директории departments, areas, journal_lists
4) В директории departments создать файл dep_list с содержимым
```
1. Pilotage service
2. Traffic management service
3. Tugboat service
4. Hydrographic service
5. Emergency rescue service
6. Security service
```
5) В директории areas создать файл area_list с содержимым
```
1. An external raid
2. Internal raid
3. Gateways
4. Mooring lines
5. Warehouses
6. Administrative and industrial buildings
7. Ship repair area
```
6) В директории journal_lists создать файл с именем copy_list 
7) Вывести полученную структуру командой tree
8) В home_works создать директорию seaport_backup
9) Скопировать содержимое seaport в seaport_backup
10) В home_works создать директорию backups
11) Переместить seaport_backup в backups
12) Переименовать seaport_backup в copy_seaport 
13) Создать файл list_of_bk в директории home_works и записать в него вывод команды ```ls -1 backups```
14) Скопировать файл list_of_bk в директорию journal_lists
