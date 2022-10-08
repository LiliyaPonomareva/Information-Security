---
## Front matter
lang: ru-RU
title: "Лабораторная работа №5"
subtitle: "Дискреционное разграничение прав в Linux. Исследование влияния дополнительных атрибутов."
author:
    Лилия М. Пономарёва
    НПИбд-02-19\inst{1}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2022, 19 March, Moscow, Russian Federation  

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
 - \usepackage[T2A]{fontenc}
 - \usepackage{amsmath}
aspectratio: 43
section-titles: true
---

# Цель работы

Изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов. Получение практических навыков работы в консоли с дополнительными атрибутами. Рассмотрение работы механизма смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.

# Создала программу simpleid.c

![Код программы simpleid.c](../../image/2.png){ #fig:001 width=80% height=80% }

# Компилирование и запуск программы

![Компиляция и выполнение программы](../../image/3.png){ #fig:001 width=80% height=80% }

# Усложнение программы

![Программа simpleid2.c](../../image/4.png){ #fig:001 width=80% height=80% }

# Работа второй программы 

![Вывод реальных и действительных идентификаторов](../../image/5.png){ #fig:001 width=80% height=80% }

# Смена владельца и группы файла simpleid2 и его прав доступа

![Смена владельца файла и прав доступа](../../image/6.png){ #fig:001 width=80% height=80% }

# Правильность установки новых атрибутов

![Вывод программы simpleid2](../../image/7.png){ #fig:001 width=80% height=80% }

# Проделали тоже самое относительно SetGID-бита

![SetGID-бит](../../image/26.png){ #fig:001 width=80% height=80% }

# Программа readfile.c 

![Код программы readfile.c](../../image/8.png){ #fig:001 width=80% height=80% }

# Компиляция readfile.c

![Компиляция](../../image/9.png){ #fig:001 width=80% height=80% }

# Смена владельца файла readfile.c

![Смена владельца файла](../../image/10.png){ #fig:001 width=80% height=80% }

# Изменение прав

![Смена атрибутов](../../image/11.png){ #fig:001 width=80% height=80% }

# Проверка

![Проверка доступа к файлу](../../image/12.png){ #fig:001 width=80% height=80% }

# Смена владельца и установка SetUID-бит

![Смена владельца и добавление SetUID у readfile](../../image/13.png){ #fig:001 width=80% height=80% }

# Выполнение программы reafile

![Чтение файла readfile.c программой readfile](../../image/14.png){ #fig:001 width=80% height=80% }

# Чтение файла /etc/shadow

![Чтение файла /etc/shadow программой из readfile](../../image/15.png){ #fig:001 width=80% height=80% }

# Наличие атрибута Sticky на директории /tmp

![Атрибут Sticky на директории /tmp](../../image/16.png){ #fig:001 width=80% height=80% }

# Создали файл file01.txt в директории /tmp со словом test

![Создание файла file01.txt в директории /tmp](../../image/17.png){ #fig:001 width=80% height=80% }

# Чтение и запись для категории пользователей «все остальные»

![Чтение и запись для категории пользователей «все остальные»](../../image/18.png){ #fig:001 width=80% height=80% }

# От пользователя guest2 прочитали файл /tmp/file01.txt

![Чтение файла /tmp/file01.txt](../../image/19.png){ #fig:001 width=80% height=80% }

# От пользователя guest2 дозаписали файл /tmp/file01.txt

![Дозапись файла /tmp/file01.txt](../../image/27.png){ #fig:001 width=80% height=80% }

# От пользователя guest2 перезапись файла /tmp/file01.txt

![Перезапись файла /tmp/file01.txt](../../image/20.png){ #fig:001 width=80% height=80% }

# Попытка удалить файл /tmp/file01.txt

![Попытка удаления файла /tmp/file01.txt](../../image/21.png){ #fig:001 width=80% height=80% }

# Сняли атрибут t (Sticky-бит) с директории /tmp

![Снятие Sticky-бит](../../image/22.png){ #fig:001 width=80% height=80% }

# От пользователя guest2 проверили, что атрибута t у директории /tmp нет

![Проверка атрибутов](../../image/23.png){ #fig:001 width=80% height=80% }

# Повторили предыдущие шаги

![Проверка атрибутов](../../image/24.png){ #fig:001 width=80% height=80% }


# Вывод

Изучили механизмы изменения идентификаторов, применения SetUID- и Sticky-битов.

