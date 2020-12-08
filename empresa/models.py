from django.db import models
from django.contrib.auth.models import User

class AuthUser(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Historial(AuthUser):
    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"
    nombre = models.TextField() 
    def __str__(self):
        return self.historial

class Estado(AuthUser):
    nombre_estado = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Evidencia(AuthUser):
    class Meta:
        verbose_name = "Evidencia"
        verbose_name_plural = "Evidencias"
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='cars')
    def __str__(self):
        return self.nombre

class TipoServicio(AuthUser):
    nombre = models.CharField(max_length=255)
    usuario= models.ForeignKey(User, null=True, blank=True, on_delete=models.RESTRICT)
    def __str__(self):
        return self.nombre

class Empresa(AuthUser):
    nombre = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    nit = models.IntegerField(unique=True)
    ciudad = models.TextField(null=True)
    direccion = models.TextField(null=True)
    departamento = models.TextField(null=True)
    logo = models.ImageField(upload_to='cars')
    def __str__(self):
        return self.nombre
    
class Guia(AuthUser):
    class Meta:
        verbose_name = "Guia"
        verbose_name_plural = "Guias"
    numero = models.IntegerField(unique=True)

class Perfil(models.Model):
    celular = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Persona(AuthUser):
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
    guia_id = models.ForeignKey(
        Guia, null=True, blank=True, on_delete=models.RESTRICT)
    evidencia_id = models.ForeignKey(
        Evidencia, null=True, blank=True, on_delete=models.RESTRICT)
    historial_id = models.ForeignKey(
        Historial, null=True, blank=True, on_delete=models.RESTRICT)
    nombres = models.TextField(null=True, max_length=50)
    apellidos = models.TextField(null=True, max_length=50)
    celular = models.IntegerField(null=False)
    whatsapp = models.IntegerField(null=True)
    correo = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    ciudad = models.TextField(null=True)
    departamento = models.TextField(null=True)   
    def __str__(self):
        return self.nombres

class Planilla(AuthUser):
    nombre = models.IntegerField(unique=True)   
    persona_id = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.RESTRICT, related_name='persona_repair')
    empresa_id = models.ForeignKey(
        Empresa, null=True, blank=True, on_delete=models.RESTRICT, related_name='empresa_repair')
    estado_id = models.ForeignKey(
        Estado, null=True, blank=True, on_delete=models.RESTRICT, related_name='estado_repair')
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.RESTRICT, related_name='usuario_repair')
    tipo_servicio = models.TextField(null=True)
    total_envios = models.IntegerField(null=True) 
    fecha_estado = models.DateField(max_length=255, null=True)
    fecha_ingreso = models.DateField(max_length=255, null=True) 
    def __str__(self):
        return self.nombres
