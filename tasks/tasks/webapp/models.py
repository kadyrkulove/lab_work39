from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, null=False, blank=False, default='new', verbose_name='Статус')

    def __str__(self):
        return f'{self.pk}. self.name (self.status)'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'