import csv

from django.conf import settings
from django.core.management import BaseCommand

from categories.models import Category
from genres.models import Genre
from reviews.models import Comment, Review
from titles.models import Title
from users.models import CustomUser


TABLES = {
    Category: 'category.csv',
    Comment: 'comments.csv',
    Genre: 'genre.csv',
    Review: 'review.csv',
    Title: 'titles.csv',
    CustomUser: 'users.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, file in TABLES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file}',
                'r',
                encoding='utf-8'
            ) as file_csv:
                reader = csv.DictReader(file_csv)
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('данные из файлов загружены'))
