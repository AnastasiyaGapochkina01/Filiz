1) Задать словарь, описывающий курс по DevOps:
```
course = {
    "title": "DevOps from zero to hero",
    "duration": "6 month",
    "price": 150000,
    "themes": ["Linux", "Web Servers", "Databases", "Docker", "Ansible", "Python", "Cloud"],
    "groups_count": 3,
    "students_count": 15
  }
```
2) Вывести словарь на экран в формате
```
Cources info
title - DevOps from zero to hero
duration - 6 month
price - 150000
themes - ['Linux', 'Web Servers', 'Databases', 'Docker', 'Ansible', 'Python', 'Cloud']
groups_count - 3
students_count - 15
```
3) Переменная students_count содержит количество студентов в одной группе. Посчитать и вывести на экран сколько всего студентов на курсе
4) Добавить в словарь course ключ "lessons_count" со значением 2. Это будет количество занятий в неделю для одной группы
5) Посчитать и вывести на экран сколько занятий для всех групп будет проведено в месяц
6) Добавить в словарь course ключ "lector_payment" со значением 5000 - сколько получает лектор за одно занятие
7) Посчитать сколько заработает лектор за месяц, если он ведет занятия у всех трех групп
