from django.contrib import admin
from django import forms

from . import models


class studentAdminForm(forms.ModelForm):

    class Meta:
        model = models.student
        fields = "__all__"


class studentAdmin(admin.ModelAdmin):
    form = studentAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.student, studentAdmin)
