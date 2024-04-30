from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'image']  # Добавляем поле изображения

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False  # Делаем поле изображения необязательным
        self.fields['image'].widget.attrs['accept'] = 'image/*'  # Добавляем атрибут accept для ограничения загрузки только изображений

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2 символов')
        return title




# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('title','text','author','status','category')
#         labels = {
#             'title': 'Заголовок',
#             'description': 'Описание',
#             'price': 'Цена',
#             'category': 'Категория',
#         }
#