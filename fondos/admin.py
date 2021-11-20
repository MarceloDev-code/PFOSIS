from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.


@admin.register(models.publicaciones)
class publicaciones_admin(admin.ModelAdmin):
    list_display = (
        'id',
    )
    list_filter = [
        'dimension',
        'autor',
    ]
    search_fields = [
        'dimension'
    ]

@admin.register(models.rol)
class rol_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'tipo',
    )

@admin.register(models.estado)
class estado_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )
@admin.register(models.dimensiones)
class dimensiones_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )
