from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.models import Group



class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name']  # Puedes agregar más campos si es necesario
        #widgets = {}
        labels = {
            'name': 'Nombre'
        }

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Aplicar')
        )
