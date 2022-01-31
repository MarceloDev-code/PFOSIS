from django import forms
from fondos.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, HTML, Div, Fieldset, Hidden, ButtonHolder, Button
from crispy_forms.bootstrap import InlineCheckboxes


class publicacionForm(forms.ModelForm):


    class Meta:
        model = publicaciones
        fields = (
            'nombre_fondo',
            'dimension',
            'descripción',
            'objetivo',
            'enlace',
            'fecha_inicio',
            'fecha_termino',

        )

        widgets = {
            'dimension': forms.Select(),
            'fecha_inicio': forms.DateTimeInput(format="%d/%m/%Y %H:%M",
                                            attrs={'type': 'date', 'class': 'form-control dtpicker', 'required': 'true'}),
            'fecha_termino': forms.DateTimeInput(format="%d/%m/%Y %H:%M",
                                             attrs={'type': 'date','class': 'form-control dtpicker', 'required': 'true'})
        }

        def __init__(self, *args, **kwargs):
            self.publicacion = kwargs.pop("publicacion")
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()

