from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from easy_pdf.views import PDFTemplateResponseMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Text

class IndexView(TemplateView):
    template_name = 'index.html'


class TextListView(LoginRequiredMixin, ListView):
    model = Text
    template_name = 'text_list.html'
    login_url = 'login'
    redirect_field_name = 'text-list'

    def get_context_data(self, **kwargs):
        context = super(TextListView, self).get_context_data(**kwargs)
        #lang = translation.get_language() #ler o idioma do navegador
        context['text'] = Text.objects.all().filter(user=self.request.user)
        return context


class TextCreateView(CreateView):
    model = Text
    template_name = 'text_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('text-list')


class TextDetailView(DetailView):
    model = Text
    template_name = 'text_detail.html'


class TextUpdateView(UpdateView):
    model = Text
    fields = ['title', 'content']
    template_name = 'text_update.html'
    success_url = reverse_lazy('text-detail')


class TextDeleteView(DeleteView):
    model = Text
    template_name = 'text_delete.html'
    success_url = reverse_lazy('text-list')


class PDFDownload(PDFTemplateResponseMixin, DetailView):
    model = Text
    template_name = 'text_download.html'
