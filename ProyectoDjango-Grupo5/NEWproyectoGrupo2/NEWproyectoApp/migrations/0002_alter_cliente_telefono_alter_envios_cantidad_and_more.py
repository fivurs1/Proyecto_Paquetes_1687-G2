# Generated by Django 4.1.2 on 2022-10-14 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWproyectoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='envios',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='envios',
            name='idEnvios',
            field=models.BigIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idFactura',
            field=models.BigIntegerField(max_length=30),
        ),
    ]