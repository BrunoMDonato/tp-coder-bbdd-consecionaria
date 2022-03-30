from django import forms

class Form_autos(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    kms = forms.IntegerField()
    anio = forms.IntegerField()
    chasis= forms.IntegerField()

class Form_motos(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    kms = forms.IntegerField()
    anio = forms.IntegerField()
    chasis = forms.IntegerField()

class Forms_vend(forms.Form):
    id_vend = forms.IntegerField()
    nombre = forms.CharField(max_length=20)
