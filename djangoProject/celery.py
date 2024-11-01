from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем Django настройку модуля по умолчанию для 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')


# Создаем приложение Celery
app = Celery('myproject')

# Загружаем настройки из Django config
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит задачи в приложениях
app.autodiscover_tasks()
