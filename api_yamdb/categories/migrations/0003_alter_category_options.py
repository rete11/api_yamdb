# Generated by Django 3.2 on 2023-12-07 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20231206_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]