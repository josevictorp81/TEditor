from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from easy_pdf.views import PDFTemplateResponseMixin

from .models import Text

class Index(TemplateView):
    template_name = 'index.html'


class TextListView(ListView):
    model = Text
    template_name = 'text_list.html'


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
    success_url = reverse_lazy('text_detail')


class TextDeleteView(DeleteView):
    model = Text
    template_name = 'text_delete.html'
    success_url = reverse_lazy('text-list')


class PDFDownload(PDFTemplateResponseMixin, DetailView):
    model = Text
    template_name = 'pdf.html'
