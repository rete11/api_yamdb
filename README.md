
# Установка
1. Сделать git clone проекта
2. Установить окружение python -m venv venv
3. Обновить pip: python -m pip install --upgrade pip
4. Установить зависимости: pip install -r requirements.py
5. Перейти в директорию с файлом manage.py: cd .\yatube_api\
6. Выполнить миграции: python manage.py migrate
7. Запустить проект: python manage.py runserver


# Примеры запросов
Добавление жанра
curl --location 'http://127.0.0.1:8000/api/v1/genres/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ***' \
--data '{
  "name": "admin-genre",
  "slug": "admin-genre-slug"
}'
Пример ответа:
{
    "name": "admin-genre",
    "slug": "admin-genre-slug"
}

Добавление категории:
curl --location 'http://127.0.0.1:8000/api/v1/categories/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ***' \
--data '{
  "name": "admin-category",
  "slug": "admin-slug"
}'
Пример ответа:
{
    "name": "admin-category",
    "slug": "admin-slug"
}

Создание произведения:
curl --location 'http://127.0.0.1:8000/api/v1/titles/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ***' \
--data '{
    "name": "Admin Title",
    "year": 2020,
    "description": "Test title by admin",
    "genre": [
        "admin-genre-slug"
    ],
    "category": "admin-slug"
}'
Пример ответа:
{
    "id": 2,
    "category": {
        "name": "admin-category",
        "slug": "admin-slug"
    },
    "genre": [
        {
            "name": "admin-genre",
            "slug": "admin-genre-slug"
        }
    ],
    "rating": null,
    "name": "Admin Title",
    "year": 2020,
    "description": "Test title by admin"
}

Добавление отзыва:
curl --location 'http://127.0.0.1:8000/api/v1/titles/2/reviews/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ***' \
--data '{
    "text": "User review",
    "score": 4
}'
Пример ответа:
{
    "id": 2,
    "author": "root",
    "score": 4,
    "text": "User review",
    "pub_date": "2023-12-07T17:33:37.217436Z",
    "title": 2
}

Добавление комментария
curl --location 'http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ***' \
--data '{
    "text": "User comment_2"
}'

Пример ответа:
{
    "id": 1,
    "author": "root",
    "text": "User comment_2",
    "pub_date": "2023-12-07T07:53:35.536450Z",
    "review": 1
}

Остальные примеры можно посмотреть в документации по эндпоинту: redoc/
