# Generated by Django 5.1.1 on 2024-09-15 03:00

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar', '0002_alter_personajes_arma_alter_personajes_vision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajes',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/images'), upload_to=''),
        ),
    ]