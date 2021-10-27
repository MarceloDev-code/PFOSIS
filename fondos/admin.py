from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.


@admin.register(models.publicaciones)
class publicaciones(admin.ModelAdmin):
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
class rol(admin.ModelAdmin):
    list_display = (
        'id',
    )


@admin.register(models.dimensiones)
class rol(admin.ModelAdmin):
    list_display = (
        'id',
    )