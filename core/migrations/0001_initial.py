# Generated by Django 3.2.4 on 2021-07-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('numero_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de Id')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagen')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=12, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('pais', models.CharField(max_length=19, verbose_name='Pais')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('moneda', models.IntegerField(choices=[[0, 'Pesos'], [1, 'Dólares']], verbose_name='moneda')),
            ],
        ),
    ]
