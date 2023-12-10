from django import forms
from .models import CustomModel

# Create your forms here.

class CustomForm(forms.ModelForm):
    class Meta:
        model = CustomModel
        fields = "__all__"