# Back-End-Developer-Capstone-LittleLemon
## Django, DRF, CSS, HTML, JavaScript

```
project-level: littlelemon/
app-level: LittleLemonAPI/, restaurant/
```

```
SupperUser:
    username: admin
    pass: admin
    token: 3d34100b7de7711ed02b2dbaaa438128a0eb693b

Another User (username - pass - token):
    HarryPotter - 123456a@ - c48efe6791c73d7048ed81d65fe87eb4a76cd2f7

```


```
1. User - Auth (with djoser)
    Create User: http://127.0.0.1:8000/auth/users/
    POST Token: http://127.0.0.1:8000/auth/token/login/
                http://127.0.0.1:8000/api/api-token-auth/
```

```
    2. api
    List, Create MenuItem: http://127.0.0.1:8000/api/menu-items
    GET, PUT, PATCH, DELETE MenuItem: http://127.0.0.1:8000/api/menu-items/<int:pk>
```

```
    3. Restaurant
    GET, POST menu items: http://127.0.0.1:8000/restaurant/menu-items
    GET, PUT, PATCH, DELETE menu items: http://127.0.0.1:8000/restaurant/menu-items/2
    GET, POST booking table: http://127.0.0.1:8000/restaurant/booking/tables
    GET, PUT, PATCH, DELETE booking items: http://127.0.0.1:8000/restaurant/booking/tables/1
```

```
#tree -L 2
├── LittleLemonAPI
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── littlelemon
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── tests
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── restaurant
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── serializers.py
    ├── static
    ├── templates
    ├── urls.py
    └── views.py
```
