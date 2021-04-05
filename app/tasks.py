from __future__ import absolute_import, unicode_literals

from django_redis_celery.celery import app

@app.task()
def add(x, y):
    return x + y