from django.shortcuts import render

from news_app.models import Article, Rubric


def set_context(data):
    rubrics = Rubric.objects.all()
    return {'rubrics': rubrics, **data}


def article_view(request):
    articles = Article.objects.all().order_by('-date')[:10]
    for article in articles:
        article.text = article.text[:50] + '...'
    return render(request, template_name='articles.html', context=set_context({'articles': articles}))


def article_filter_view(request, rubric):
    articles = Article.objects.filter(rubric__url_name=rubric).order_by('-date')[:10]
    for article in articles:
        article.text = article.text[:50] + '...'
    return render(request, template_name='articles.html', context=set_context({'articles': articles}))


def article_item_view(request, id):
    article = Article.objects.get(pk=id)
    return render(request, template_name='article_item.html', context=set_context({'article': article}))
