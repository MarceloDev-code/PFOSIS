from django.db import models
from fondos.models import *
from django.contrib.auth.models import User
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year


class calendar(models.Model):

    nombre = models.CharField(
        max_length=255
    )
    anio = models.IntegerField(
        verbose_name="Año",
        default=current_year
    )

    class Meta:
        verbose_name = 'Calendario de fondos'
        verbose_name_plural = 'Calendarios'

    def save(self, *args, **kwargs):
        calendar.objects.exclude(pk=self.pk).update(activo=False)
        return super(calendar, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(
            self.nombre,
            self.anio,
        )

