from uuid import uuid4

from django.db import models


class Student(models.Model):
    """
    Модель сущности "Студент"
    """
    uid = models.UUIDField(primary_key=True, default=uuid4)
    firstname = models.CharField(max_length=128, verbose_name='Имя')
    lastname = models.CharField(max_length=128, verbose_name='Фамилия')
    university = models.CharField(max_length=128, verbose_name='Образование')
    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    comment = models.TextField(max_length=512, blank=True, verbose_name='Примечание')
    is_active = models.BooleanField(default=True, verbose_name='Пользователь активен?')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
