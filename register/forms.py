from django import forms
from .models import govt_sign

class application_form(forms.ModelForm):
    class Meta:
        model = govt_sign
        fields = ['firstname', 'lastname', 'documents', 'photo']