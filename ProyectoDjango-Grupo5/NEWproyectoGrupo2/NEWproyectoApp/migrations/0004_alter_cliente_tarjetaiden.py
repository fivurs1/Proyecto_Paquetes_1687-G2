# Generated by Django 4.1.2 on 2022-10-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWproyectoApp', '0003_alter_cliente_tarjetaiden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='TarjetaIden',
            field=models.BigIntegerField(),
        ),
    ]
