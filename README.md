### Описание проекта:

Тестовое задание ,  создал API на основе Django Rest Framework для  сервиса, который принимает запрос с указанием кадастрового номера, широты и долготы, отправляет запрос на внешний сервер. Затем должен отдавать результат запроса


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:


```
cd tests
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Запуск через Докер

Сначала запустите докер 

```
docker run
```

```
docker-compose up -d
```

### Примеры запросов к API:
http://127.0.0.1:8000/api/v1/history
```
   {
        "cadastral_number": 1,
        "width": 1,
        "longitude": 23
   }
```

http://127.0.0.1:8000/api/v1/ping
```
    {
        "status": "Работает"
    }
```

http://127.0.0.1:8000/api/v1/result/1/ получение результата по кадастровому номеру

```

    {
        "width": 1,
        "longitude": 23,
        "status": false
    },
    {
        "width": 1,
        "longitude": 2332,
        "status": true
    },
```

Документация к API
```
http://127.0.0.1:8000/swagger/
```
