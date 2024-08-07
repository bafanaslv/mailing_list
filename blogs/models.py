from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='mailing/media', verbose_name='изображение', help_text='загрузите изображение', **NULLABLE)
    view_counter = models.PositiveIntegerField(default=0, verbose_name='счетчик проcмотров', help_text='укажите количество просмотров')
    data_publish = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
