from django.db import models


class Record(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана(получена от локального сервера)'),
    ]

    timestamp = models.DateTimeField('Дата и время действия')
    status = models.CharField('Статус', max_length=35, choices=STATUS_CHOICES)
    change = models.JSONField()
    author = models.CharField('Источник изменения', max_length=20)





