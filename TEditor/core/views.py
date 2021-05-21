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

    def get_context_data(self, **kwargs):
        context = super(TextListView, self).get_context_data(**kwargs)
        context['text'] = Text.objects.all().filter(user=self.request.user)
        return context

# trocar por uma funcao
class TextCreateView(LoginRequiredMixin, CreateView):
    model = Text
    template_name = 'text_create.html'
    fields = ['title', 'content', 'user']
    success_url = reverse_lazy('text-list')
    login_url = 'login'


class TextDetailView(LoginRequiredMixin, DetailView):
    model = Text
    template_name = 'text_detail.html'
    login_url = 'login'


class TextUpdateView(LoginRequiredMixin, UpdateView):
    model = Text
    fields = ['title', 'content']
    template_name = 'text_update.html'
    login_url = 'login'


class TextDeleteView(LoginRequiredMixin, DeleteView):
    model = Text
    template_name = 'text_delete.html'
    success_url = reverse_lazy('text-list')
    login_url = 'login'


class PDFDownload(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Text
    template_name = 'text_download.html'
    login_url = 'login'
