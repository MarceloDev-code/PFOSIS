from django import forms
from crispy_forms.layout import Layout, Div, Field
from crispy_forms.helper import FormHelper
from models import *
from django.utils import timezone


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = calendar
        fields = (
            'nombre',
            'anio',
        )

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'anio': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Field(
                        'nombre',
                    ),
                    css_class="col-md-6"
                ),
                Div(
                    Field(
                        'anio',
                    ),
                    css_class="col-md-6"
                ),

                css_class="row",
            ),
        )