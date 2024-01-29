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

'''  
class Boleta(models.Model):
    id_boleta = models.AutoField(db_column='id_boleta', primary_key=True)
    fecha = models.DateField(blank=False, null=False)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='rut')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='idproducto')
    total = models.IntegerField(blank=False, null=False)
    metodo_pago = models.CharField(max_length=20, blank=False, null=False)
    estado_choices = [
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    estado = models.CharField(max_length=9, choices=estado_choices, blank=False, null=False)

    def __str__(self):
        return str(self.id_boleta)+" "+str(self.fecha)+" "+str(self.cliente)+" "+str(self.total)
    
    #def cliente_info(self):
        return str(self.cliente.rut)+" "+str(self.cliente.nombre)+" "+str(self.cliente.ap_paterno)
    
    #def producto_info(self):
        return str(self.producto.id_producto)+" "+str(self.producto.marca)+" "+str(self.producto.modelo)
'''