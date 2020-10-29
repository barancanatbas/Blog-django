from django import forms
from .models import reports,Kategori

class reportsForm(forms.ModelForm):
    class Meta():
        model = reports
        fields =[
            'name',
            'title',
            'email',
            'content',
        ]

        