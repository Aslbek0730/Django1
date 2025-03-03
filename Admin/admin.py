from django.contrib import admin
from django import forms

from . import models


class AdminAdminForm(forms.ModelForm):

    class Meta:
        model = models.Admin
        fields = "__all__"


class AdminAdmin(admin.ModelAdmin):
    form = AdminAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Admin, AdminAdmin)
