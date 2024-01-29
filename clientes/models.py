from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class ClienteManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Por favor, ingrese un correo electrónico válido.')
        if not password:
            raise ValueError('Por favor, ingrese una contraseña válida.')
        email =self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Cliente(AbstractBaseUser, PermissionsMixin):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, blank=False, null=True)
    first_name = models.CharField(max_length=25, blank=False, null=True)
    last_name = models.CharField(max_length=25, blank=False, null=True)
    ap_materno = models.CharField(max_length=25, blank=False, null=True)
    fec_nac = models.DateField(blank=False, null=True)
    tele = models.IntegerField(blank=False, null=True) #Usar validaciones con expresiones regulares para el largo de ocho dígitos...
    region = models.CharField(max_length=20, blank=False, null=True)
    ciudad = models.CharField(max_length=20, blank=False, null=True)
    comuna = models.CharField(max_length=20, blank=False, null=True)
    dire = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=40, blank=False, null=False, unique=True)
    password = models.CharField(max_length=15, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut']

    def __str__(self):
        return str(self.rut)+ " " +str(self.first_name)+ " " +str(self.last_name)+ " " +str(self.ap_materno)
    


    
