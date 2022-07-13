## Тестовое задание для проекта Вселен
Требуется развернуть проект DRF, создать модель Студенты и реализовать методы get, post
### Реализация
Задание реализовано на Python 3.9 с использованием фреймворка Django/DjangoRestFramework. 
В качестве СУБД используется SQLite, при деплое возможно применение PostgreSQL путем изменения параметра ENV_TYPE на 'prod' в переменных окружения. 
Сервис покрыт тестами посредством Unittest.
### Запуск проекта
Для запуска проекта необходимо:
1. Создать виртуальное окружение и активировать его
```angular2html
$ python3 -m venv env
$ source env/bin/activate
```
2. Установить зависимости из файла requirements.txt
```angular2html
$ cd vselen/
$ pip3 install -r requirements.txt
```
3. Создать файл .env и записать в него параметры из файла .env.sample
4. Применить миграции
```angular2html
$ python3 manage.py migrate
```
5. Выполнить запуск Django проекта
```angular2html
$ python3 manage.py runserver
```

### Документация по API
Документация размещена по адресам:
#### http://127.0.0.1:8000/swagger/
#### http://127.0.0.1:8000/redoc/
