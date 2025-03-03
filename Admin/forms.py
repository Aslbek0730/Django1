from django import forms
from . import models


class AdminForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = []

