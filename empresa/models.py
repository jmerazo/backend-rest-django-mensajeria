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

    nombre_historial = models.TextField() 

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

    def __str__(self):
        return self.nombre


class Empresa(AuthUser):

    nombre = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    nit = models.IntegerField()
    ciudad_empresa = models.TextField(null=True)
    direccion_empresa = models.TextField(null=True)
    departamento_empresa = models.TextField(null=True)
    logo = models.ImageField(upload_to='cars')

    def __str__(self):
        return self.nombre


class Terceros(AuthUser):
    class Meta:
        verbose_name = "Tercero"
        verbose_name_plural = "Terceros"

    guia_numero = models.IntegerField()
    nombre_tercero = models.TextField(null=True)
    tipo_servicio = models.ForeignKey(
        TipoServicio, null=True, blank=True, on_delete=models.RESTRICT)
    ciudad_tercero = models.TextField(null=True)
    fecha_estado = models.DateField(max_length=255, null=True)
    fecha_ingreso = models.DateField(max_length=255, null=True)
    tracking_terceros = models.CharField(max_length=255, null=True)
    historial_id = models.ForeignKey(
        Historial, null=True, blank=True, on_delete=models.RESTRICT)
    estado_id = models.ForeignKey(
        Estado, null=True, blank=True, on_delete=models.RESTRICT)
    empresa_id = models.ForeignKey(
        Empresa, null=True, blank=True, on_delete=models.RESTRICT)
    evidencia_id = models.ForeignKey(
        Evidencia, null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre_tercero
