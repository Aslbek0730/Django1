from django import forms
from . import models


class studentForm(forms.ModelForm):
    class Meta:
        model = models.student
        fields = []

