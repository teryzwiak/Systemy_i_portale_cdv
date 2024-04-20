from django import forms
from .models import CustomTable

class CreateTableForm(forms.ModelForm):
    class Meta:
        model = CustomTable
        fields = ['table_name']