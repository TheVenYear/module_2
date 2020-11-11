from django.contrib import admin

from news_app.models import Article, Rubric


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'date')


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')