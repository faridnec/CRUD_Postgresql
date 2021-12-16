from django import forms
from CRUD_Uygulama.models import Calisan


class Form(forms.ModelForm):
    class Meta:
        model = Calisan
        fields = "__all__"
