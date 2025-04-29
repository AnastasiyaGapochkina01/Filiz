## Концепт
Игрок просыпается в подземелье таинственного замка, охваченного заклятием. Цель — исследовать замок, решать головоломки, находить предметы и так дойти до конца
## Персонаж
У персонажа есть
- имя (character_name) - вводится пользователем при старте игры
- здоровье (hp): начальное значение = 3. При значении hp 0 игра завершается
- инвентарь - игрок может хранить до 3 предметов
## Локации
### Старт - подземелье
#### Описание
You wake up in a damp dungeon. The light of the torch barely illuminates the stone walls. There is a heavy iron door in front of you. On the right is a pile of crates, on the left is a pool of blood.
#### Возможые действия
* 1 - осмотреть ящики → находка: ржавый ключ (добавляется в инвентарь)
* 2 - попытаться выбить дверь → потеря 1 point от hp (ловушка). Если hp = 0 → Концовка: "You died from your wounds".
* 3 - искать скрытый рычаг → успех → переход в локацию "коридор"
### "коридор"
#### Описание
You are in a long corridor with torches on the walls. There are claw marks on the floor. Two doors: to the left (library) and to the right (kitchen). At the end of the corridor is a staircase to the top.
#### Возможые действия
* left: Библиотека → Переход в локацию "библиотека"
* right: Кухня → Переход в локацию "кухня".
* up: Подняться по лестнице → Требуется ключ. Если есть ржавый ключ → переход в "Зал Призрака". Иначе → "Дверь заперта!".
### "библиотека"
#### Описание
Shelves with dusty books. On the table is an open folio and a silver key. The window is barred.
#### Возможые действия
* key: Взять серебряный ключ → Добавляется в инвентарь.
* book: Прочитать книгу → Подсказка: "Ответ на загадку Призрака — 'путь'".
* back: Вернуться в коридор → Переход в локацию "коридор"
### "кухня"
#### Описание
Musty smell. There's a knife and moldy bread on the table. There's a locked chest in the corner.
#### Возможые действия
* knife: Взять нож → Добавляется в инвентарь.
* eat: Съесть хлеб → Восстанавливает 1 point hp.
* open: Открыть сундук → Если есть нож → внутри золотой ключ. Иначе → "Сундук не поддается".
### Зал Призрака
#### Описание
In the center of the hall is a ghost in armor. He says, "Answer the riddle, mortal: 'What do you lose as soon as you find it?'".
#### Загадка
- Правильный ответ ("путь") → Призрак исчезает. Открывается проход в Сокровищницу.
- Неправильный ответ → Призрак атакует. Если есть нож → побег в коридор. Иначе → Концовка: "Ваша душа стала частью замка".
### Сокровищница
#### Описание
A room with a chest and a secret door to freedom. There is an inscription on the chest: "Only the worthy owner of the key."
#### Возможые действия
- open: Открыть сундук (золотой ключ) → Концовка: "Вы нашли сокровища!".
- out: Выйти через дверь → Концовка: "Вы сбежали из замка!".
### Башня (альтернативный путь)
Доступна только если игрок нашел серебряный ключ в библиотеке
#### Описание
You are at the top of the tower. In front of you is a cage with a white ghost. He whispers, "Set me free..."
#### Возможые действия
* 1: Открыть клетку (серебряный ключ) → Концовка: "Вы сняли проклятие замка!".
* 2: Уйти → Возврат в коридор.
