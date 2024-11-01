from celery import shared_task
from .models import Article
from datetime import datetime

@shared_task
def create_article(title, content):
    article = Article.objects.create(title=title, content=content, published_date=datetime.now())
    return f"Article '{article.title}' created with ID {article.id}"
