from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    url_name = models.SlugField(max_length=50, verbose_name='url новости', default='none')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тематика'
        verbose_name_plural = 'тематики'


class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    text = models.TextField(verbose_name='текст')
    rubric = models.ForeignKey(to=Rubric, on_delete=models.SET_NULL, null=True, related_name='articles',
                               verbose_name='тематика')
    image = models.ImageField(upload_to='news/', verbose_name='изображение', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

