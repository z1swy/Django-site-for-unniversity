# Проект образовательной платформы университета

## Настройка

Для запуска нужно установить python

Виртуальное окружение:

```sh
python3 -m venv env
source env/bin/activate
```

Установка библиотек:

```sh
pip install -r requirements.txt
```

## Команды для разработки

### Запуск в режиме разработки

```sh
python3 manage.py runserver
```

### Создание миграций для приложения

```sh
python3 manage.py makemigrations <название приложения>
```

### Выполнение миграций

```sh
python3 manage.py migrate
```

### Создание стартовых данных для БД

```sh
python3 manage.py dumpdata -o initial_data.json
```

### Загрузка стартовых данных в БД

```sh
python3 manage.py loaddata initial_data.json
```

### Создание суперпользователя

```sh
python3 manage.py createsuperuser
```

## Работа с git

### Посмотреть все ветки
```sh
git branch
```

### Создание новой ветки 
```sh
git checkout -b <new_branch>
```

### Добавление всех файлов в индекс
```sh
git add -A
```

### Создание коммита
```sh
git commit -m "Название коммита"
```

### Переименовать комит на всякий
```sh
git commit --amend -m 'Новое имя коммита'   
``` 

### Отправка изменний в github
```sh
git push
``` 

### Переключение на ветку main
```sh
git checkout main
``` 

### Загрузка изменний из github
```sh
git pull
``` 

### Удаление локальной ветки
```sh
git branch -D <branch_name>
``` 
