# Generated by Django 3.1.3 on 2020-11-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('text', models.TextField(verbose_name='текст')),
                ('image', models.ImageField(upload_to='news/', verbose_name='изображение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
            ],
        ),
    ]
