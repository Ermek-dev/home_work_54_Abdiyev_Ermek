# Generated by Django 5.0.3 on 2024-03-31 23:10

import webapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cover',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=webapp.models.user_directory_path),
        ),
    ]
