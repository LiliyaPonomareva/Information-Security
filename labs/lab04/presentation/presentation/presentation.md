---
## Front matter
lang: ru-RU
title: "Лабораторная работа №4"
subtitle: "Дискреционное разграничение прав в Linux. Расширенные атрибуты"
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

Получение практических навыков работы в консоли с расширенными
атрибутами файлов.

# Определила расширенные атрибуты файла file1

![Определение расширенных атрибутов файла](../../image/1.png){ #fig:001 width=80% height=80% }

# Установила на файл file1 права, разрешающие чтение и запись

![Права, разрешающие чтение и запись для владельца](../../image/2.png){ #fig:001 width=80% height=80% }

# Попробовала установить на файл /home/guest/dir1/file1 расширенный атрибут a

![Установка расширенного атрибута от имени обычного пользователя](../../image/3.png){ #fig:001 width=80% height=80% }

# Попробовала установить расширенный атрибут a на файл от имени суперпользователя

![Установка расширенного атрибута от имени суперпользователя](../../image/4.png){ #fig:001 width=80% height=80% }

# От пользователя guest проверила правильность установления атрибута

![Правильность установления атрибута](../../image/5.png){ #fig:001 width=80% height=80% }

# Выполнила дозапись в файл file1

![Запись и чтение файла](../../image/6.png){ #fig:001 width=80% height=80% }

# Попробовала удалить файл

![Попытка удаления файла файла](../../image/7.png){ #fig:001 width=80% height=80% }

# Попробовала перезаписать файл

![Запись в файл](../../image/14.png){ #fig:001 width=80% height=80% }

# Попробовала переименовать файл

![Попытка переименовать файл](../../image/8.png){ #fig:001 width=80% height=80% }

# Попробовала установить на файл права, запрещающие чтение и запись

![Попытка изменения прав доступа файла](../../image/9.png){ #fig:001 width=80% height=80% }

# Сняла расширенный атрибут a с файла

![Снятие расширенного атрибута а](../../image/10.png){ #fig:001 width=80% height=80% }

# Повторила операции, которые ранее не удавалось выполнить

![Повтор операций](../../image/11.png){ #fig:001 width=80% height=80% }

# Заменила атрибут «a» атрибутом «i»

![Добавление атрибута i](../../image/12.png){ #fig:001 width=80% height=80% }

# Повторила выполнение операций

![Операции с новым атрибутом](../../image/13.png){ #fig:001 width=80% height=80% }

# Вывод

Опробовали на практике действие расширенных атрибутов «а» и «i».

