from django.urls import path

from .views import *

urlpatterns = [
    path('', article_view, name='articles'),
    path('<int:id>', article_item_view, name='article_pk'),
    path('rubric/<str:rubric>', article_filter_view, name='articles_by')
]
