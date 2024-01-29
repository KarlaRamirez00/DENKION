# Generated by Django 5.0.1 on 2024-01-28 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0006_remove_cliente_producto_delete_boleta_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(blank=True, max_length=1, null=True)),
                ('nombre', models.CharField(blank=True, max_length=25, null=True)),
                ('ap_paterno', models.CharField(blank=True, max_length=25, null=True)),
                ('ap_materno', models.CharField(blank=True, max_length=25, null=True)),
                ('fec_nac', models.DateField()),
                ('tele', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=20, null=True)),
                ('comuna', models.CharField(blank=True, max_length=20, null=True)),
                ('dire', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=40, null=True)),
                ('contra', models.CharField(blank=True, max_length=15, null=True)),
                ('producto', models.ForeignKey(db_column='idproducto', default=None, on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]