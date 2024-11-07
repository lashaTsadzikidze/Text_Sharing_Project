from django import forms
from .models import SharedText

class TextForm(forms.ModelForm):
    class Meta:
        model = SharedText
        fields = ['content']