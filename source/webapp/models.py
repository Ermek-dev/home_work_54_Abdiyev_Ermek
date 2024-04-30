import os

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import uuid


def user_directory_path(instance, filename):
    # Генерируем уникальное имя файла
    unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
    # Возвращаем путь для сохранения файла
    return os.path.join('user_files', unique_filename)

class Product(models.Model):
    user = models.ForeignKey(to=User,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, blank=True, default='No description')
    category = models.ForeignKey(
        to = 'webapp.Category',
        verbose_name ='Категория',
        null = True,
        blank = False,
        related_name = 'product',
        on_delete = models.RESTRICT
    )
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    created_at = models.DateTimeField(default=timezone.now,verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(default=timezone.now,verbose_name='Дата и время обновления')
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to=user_directory_path,blank=True, null=True)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        formatted_price = '{:,.0f}'.format(self.price).replace(',', ' ')
        return f'{self.title} - {formatted_price}'

    def __str__(self):
        return f'{self.title} - {self.category}'
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'


    def delete(self,using=None,keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000,null=False,default='No description')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
