from django import forms

from .models import Text

class TextModelForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'content']
