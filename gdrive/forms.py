from django import forms
from .models import *


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('description', 'files')
