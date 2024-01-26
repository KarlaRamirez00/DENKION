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
    
class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)
    ap_paterno = models.CharField(max_length=25, blank=True, null=True)
    ap_materno = models.CharField(max_length=25, blank=True, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='idproducto', default=None)
    fec_nac = models.DateField(blank=False, null=False)
    tele = models.IntegerField(blank=True, null=True) #Usar validaciones con expresiones regulares para el largo de ocho dígitos...
    region = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    comuna = models.CharField(max_length=20, blank=True, null=True)
    dire = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(max_length=40, blank=True, null=True)
    contra = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.rut)+ " " +str(self.nombre)+ " " +str(self.ap_paterno)+ " " +str(self.ap_materno)+ " " +str(self.producto)
    
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
    