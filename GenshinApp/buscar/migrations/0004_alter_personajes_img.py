# Generated by Django 5.1.1 on 2024-09-15 03:42

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar', '0003_alter_personajes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajes',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/images'), upload_to='images/'),
        ),
    ]