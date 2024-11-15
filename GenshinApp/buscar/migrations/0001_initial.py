# Generated by Django 5.1.1 on 2024-09-14 21:44

import buscar.enums
import django.core.files.storage
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('elemental', models.CharField(max_length=75)),
                ('arma', models.CharField(choices=[(buscar.enums.TipoArmas['MANDOBLE'], 'Mandoble'), (buscar.enums.TipoArmas['ESPADA_LIGERA'], 'Espada Ligera'), (buscar.enums.TipoArmas['ARCO'], 'Arco'), (buscar.enums.TipoArmas['CATALIZADOR'], 'Catalizador'), (buscar.enums.TipoArmas['LANZA'], 'Lanza')], max_length=15)),
                ('vision', models.CharField(choices=[(buscar.enums.Vision['PYRO'], 'Pyro'), (buscar.enums.Vision['HYDRO'], 'Hydro'), (buscar.enums.Vision['DENDRO'], 'Dendro'), (buscar.enums.Vision['ELECTRO'], 'Electro'), (buscar.enums.Vision['CYRO'], 'Cyro'), (buscar.enums.Vision['GEO'], 'Geo'), (buscar.enums.Vision['ANEMO'], 'Anemo')], max_length=10)),
                ('ultimate', models.CharField(max_length=75)),
                ('decripcion', models.TextField(blank=True)),
                ('decripcion_elemental', models.TextField(blank=True)),
                ('decripcion_ultimate', models.TextField(blank=True)),
                ('img', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/images'), upload_to='images/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
