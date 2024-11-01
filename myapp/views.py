from django.shortcuts import render
from .models import Article
from django.shortcuts import render
from .models import Article
from .tasks import create_article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/article_list.html', {'articles': articles})



def article_list(request):
    articles = Article.objects.all()

    # Пример вызова задачи Celery
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        create_article.delay(title, content)

    return render(request, 'myapp/article_list.html', {'articles': articles})
