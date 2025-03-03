from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class studentListView(generic.ListView):
    model = models.student
    form_class = forms.studentForm


class studentCreateView(generic.CreateView):
    model = models.student
    form_class = forms.studentForm


class studentDetailView(generic.DetailView):
    model = models.student
    form_class = forms.studentForm


class studentUpdateView(generic.UpdateView):
    model = models.student
    form_class = forms.studentForm
    pk_url_kwarg = "pk"


class studentDeleteView(generic.DeleteView):
    model = models.student
    success_url = reverse_lazy("student_student_list")
