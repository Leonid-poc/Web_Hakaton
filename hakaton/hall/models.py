from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  first_name = models.TextField(verbose_name='Имя', blank=False)
  last_name = models.TextField(verbose_name='Фамилия', blank=False)
  middle_name = models.TextField(verbose_name='Отчество', blank=False)
  birth_day = models.DateField(verbose_name='Дата рождения', blank=False)
  email = models.EmailField(verbose_name='E-mail', blank=False)

class NewsPost(models.Model):
  title = models.TextField(verbose_name='Заголовок')
  desc = models.TextField(verbose_name='Контент')
  image = models.ImageField(verbose_name='Обложка')

  is_publish = models.BooleanField(verbose_name='Публиковать', default=False)

  create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add==True)
  edit_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
  publish_date = models.DateTimeField(verbose_name='Дата публикации')