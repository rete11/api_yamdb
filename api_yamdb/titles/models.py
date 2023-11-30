from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Title(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
