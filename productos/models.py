from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto      = models.AutoField(db_column='idproducto', primary_key=True)
    modelo           = models.CharField(max_length=20, blank=True, null=True)
    marca            = models.CharField(max_length=20, blank=True, null=True)
    anno_fab         = models.IntegerField(blank=True, null=True)
    precio           = models.IntegerField(blank=True, null=True)
    stock            = models.IntegerField(blank=True, null=True)
    estado_choices   = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ]
    estado           = models.CharField(max_length=5, choices=estado_choices, blank=True, null=True)
    categoria        = models.CharField(max_length=20, blank=True, null=True)
    desc             = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.marca)+ " " +str(self.modelo)+ " " +str(self.anno_fab)