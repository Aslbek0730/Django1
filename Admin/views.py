from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class AdminListView(generic.ListView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminCreateView(generic.CreateView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminDetailView(generic.DetailView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminUpdateView(generic.UpdateView):
    model = models.Admin
    form_class = forms.AdminForm
    pk_url_kwarg = "pk"


class AdminDeleteView(generic.DeleteView):
    model = models.Admin
    success_url = reverse_lazy("Admin_Admin_list")
