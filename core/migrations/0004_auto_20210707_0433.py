# Generated by Django 3.2.4 on 2021-07-07 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_proveedores_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monedas',
            fields=[
                ('idMoneda', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de monedas')),
                ('nombreMoneda', models.CharField(max_length=25, verbose_name='Nombre de la moneda')),
            ],
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.monedas'),
        ),
    ]
