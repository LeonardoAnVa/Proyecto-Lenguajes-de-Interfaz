from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm

from noticia.models import Reportero, Noticia


class ReporteroForm(ModelForm):
    first_name = forms.CharField(label='Nombre(s)')
    last_name = forms.CharField(label='Apellidos')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    telefono = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='deben ser 10 números.',
                code='invalid_phone_number'
            )
        ]
    )


class ReporteroForm(ModelForm):
    first_name = forms.CharField(label='Nombre(s)')
    last_name = forms.CharField(label='Apellidos')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    telefono = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='deben ser 10 números.',
                code='invalid_phone_number'
            )
        ]

    )

    def __init__(self, *args, **kwargs):
        super(ReporteroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4'),
                Column('last_name', css_class='form-group col-md-4'),
                Column('fecha_nacimiento', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-8'),
                Column('telefono', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('foto', css_class='form-group col-md-6'),
                Column('acta_nacimiento', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('username', css_class='form-group col-md-6'),
                Column('password', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Aplicar')
        )

    class Meta:
        model = Reportero
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'telefono',
            'fecha_nacimiento',
            'foto',
            'acta_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Seleccione una fecha'}),
            'foto': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }
        labels = {
            'fecha_nacimiento': 'Nacimiento'
        }


class NoticiaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('titulo', css_class='form-group col-md-6'),
                Column('autor', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'contenido',
            Row(
                Column('imagen', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
            Submit('submit', 'Aplicar')
        )

    class Meta:
        model = Noticia
        fields = ['titulo', 'autor', 'contenido', 'imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'contenido': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'titulo': 'Título la Noticia',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'imagen': 'Imagen'
        }