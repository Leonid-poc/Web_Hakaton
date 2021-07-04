from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  first_name = models.CharField(verbose_name='Имя', max_length=128, blank=False, null=True)
  last_name = models.CharField(verbose_name='Фамилия', max_length=128, blank=False, null=True)
  middle_name = models.CharField(verbose_name='Отчество', max_length=128, blank=False, null=True)
  birth_day = models.DateField(verbose_name='Дата рождения', blank=False, null=True)
  email = models.EmailField(verbose_name='E-mail', blank=False, null=True)

class NewsPost(models.Model):
  class Meta:
    verbose_name = 'Новостной пост'
    verbose_name_plural = 'Новостные посты'
  title = models.CharField(verbose_name='Заголовок', max_length=128,)
  desc = models.TextField(verbose_name='Контент')
  image = models.ImageField(verbose_name='Обложка')

  is_publish = models.BooleanField(verbose_name='Публиковать', default=False)

  create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
  edit_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
  publish_date = models.DateTimeField(verbose_name='Дата публикации')