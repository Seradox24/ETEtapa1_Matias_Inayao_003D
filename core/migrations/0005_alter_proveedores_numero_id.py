# Generated by Django 3.2.4 on 2021-07-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210707_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='numero_id',
            field=models.AutoField(default='00', primary_key=True, serialize=False, verbose_name='Numero de Id'),
        ),
    ]