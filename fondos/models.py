from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

usuario = get_user_model()

class usuario(models.Model):
    rut = models.CharField(max_length=20,unique=True,null=False,verbose_name="Documento Chileno de identificación")
    nombres = models.CharField(max_length=100,verbose_name="Nombres")
    rol = models.ForeignKey('rol',verbose_name="Rol",on_delete=models.PROTECT)

    apellidos = models.CharField(max_length=100,verbose_name="Apellidos")
    fecha_creado = models.DateTimeField(auto_created=True,verbose_name="Fecha de creación")
    fecha_editado = models.DateTimeField(auto_now=True,verbose_name="Fecha de Ultima Edición")

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['rut','rol']

    def nombre_completo(self):
        nombre_comm = self.nombres+" "+self.apellidos
        return nombre_comm

    def __str__(self):
       return "{} - {} - {}".format(
            self.nombre_completo(),
            self.rut,
            self.rol
        )

class dimensiones(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
       return "{}".format(
            self.nombre
        )

class publicaciones(models.Model):
    nombre_fondo = models.CharField(max_length=200,null=False,verbose_name="Nombre del Fondo")
    dimension = models.ForeignKey('dimensiones',verbose_name="Dimensión",on_delete=models.PROTECT)
    autor = models.ForeignKey('usuario',verbose_name="Autor",on_delete=models.PROTECT)
    objetivo = models.CharField(max_length=300,null=True,verbose_name="Objetivo")
    enlace = models.CharField(max_length=200,verbose_name="Link")
    fecha_inicio = models.DateTimeField(verbose_name="Fecha inicio")
    fecha_termino = models.DateTimeField(verbose_name="Fecha termino")

    def __str__(self):
       return "{} - {} - {} - {}".format(
            self.nombre_fondo,
            self.dimension,
            self.autor,
            self.fecha_termino
        )

class estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        "{}".format(
            self.nombre
        )
class adjudicarse_fondo(models.Model):

    subscriptor = models.ForeignKey('usuario',on_delete=models.PROTECT)
    publicacion = models.ForeignKey('publicaciones',on_delete=models.PROTECT)
    estado = models.ForeignKey('estado',on_delete=models.PROTECT)

class rol(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
       return "{}".format(
            self.tipo
        )
