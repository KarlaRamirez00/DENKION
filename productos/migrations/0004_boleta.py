# Generated by Django 5.0.1 on 2024-01-25 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_cliente_producto_alter_cliente_rut_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(db_column='id_boleta', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('metodo_pago', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], max_length=9)),
                ('cliente', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='productos.cliente')),
                ('producto', models.ForeignKey(db_column='idproducto', on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
