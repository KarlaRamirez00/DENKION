# en forms.py
from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo electrónico')
    tel = forms.CharField(label='Teléfono', required=False, max_length=8)
    tipo_con = forms.ChoiceField(label='Tipo consulta', choices=[('Servicio', 'Servicio'), ('Producto', 'Producto')])
    con = forms.CharField(label='Consulta', widget=forms.Textarea, max_length=400)

