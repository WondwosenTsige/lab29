from django.urls import reverse_lazy
from .models import Appx
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

class AppxListView(ListView):
    template_name = "pages/appx-list.html"
    model = Appx


class AppxDetailView(DetailView):
    template_name = "pages/appx-detail.html"
    model = Appx


class AppxCreateView(CreateView):
    template_name = "pages/appx-create.html"
    model = Appx
    fields = ['name', 'description', 'owner']


class AppxUpdateView(UpdateView):
    template_name = "pages/appx-update.html"
    model = Appx
    fields = ['name', 'description', 'owner']


class AppxDeleteView(DeleteView):
    template_name = "pages/appx-delete.html"
    model = Appx
    success_url = reverse_lazy("Appx_list")
