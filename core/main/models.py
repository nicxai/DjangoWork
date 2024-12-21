from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок'
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )

class Benner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    image = models.ImageField(
        upload_to='bennerImage/',
        verbose_name='Image'
    )

class Meta:
    verbose_name = 'Настройка'
    verbose_name_plural = 'Настойка'