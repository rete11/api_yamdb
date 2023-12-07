# Описание
API по учебному проекту YaMdb

# Авторы
Сергей Попов
Денис Хрущев
Виталий Бранихин

# Установка
1. Сделать git clone проекта
2. Установить окружение python -m venv venv
3. Обновить pip: python -m pip install --upgrade pip
4. Установить зависимости: pip install -r requirements.py
5. Перейти в директорию с файлом manage.py: cd .\yatube_api\
6. Выполнить миграции: python manage.py migrate
7. Запустить проект: python manage.py runserver


# Примеры запросов
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