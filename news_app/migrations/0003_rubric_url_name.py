# Generated by Django 3.1.3 on 2020-11-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20201111_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubric',
            name='url_name',
            field=models.SlugField(default='none', verbose_name='url новости'),
        ),
    ]