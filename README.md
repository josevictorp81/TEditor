# TEditor

TEditor é um editor de texto Rich Text, que dispõe de varias opções para a formatação de textos no geral. Para esta aplicação, o usuário deve criar um conta para acessar as opções de: criar, listar, editar e deletar um texto. Possuindo também uma opção para o download do texto em formato PDF.

## Bibliotecas
- [Django](https://www.djangoproject.com/)
- [django-easy-pdf](https://django-easy-pdf.readthedocs.io/en/develop/), renderiza tempaltes em PDFs.
- [Django widgets_tweaks](https://pypi.org/project/django-widget-tweaks/), biblioteca que renderiza campos de formulário em templates.
- [Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/), biblioteca que integra um editor do "WYSIWYG".

### django-easy-pdf
```
$ pip install django-easy-pdf WeasyPrint
```

Adicionando *easy_pdf* nos *INSTALLED_APPS* em `settings.py`:
```python
INSTALLED_APPS = [
    'easy_pdf',
]
```
Em `view.py`:
```python
from easy_pdf.views import PDFTemplateResponseMixin

class PDFDownload(PDFTemplateResponseMixin, DetailView):
    model = Model
    template_name = 'download.html'
```

### Django widgets_tweaks
```
$ pip install django-widget-tweaks
```
Habilitar *widget_tweaks*, adicione nos *INSTALLED_APPS* em `settings.py`:
```python
INSTALLED_APPS = [
    'widget_tweaks',
]
```

Assim, para para renderizar um campo template *HTML* usa-se a template tag `render_field`.
```python
{% load widget_tweaks %}

{% render_field form.title placeholder="input" %}
```
### Django CKEditor
```
$ pip install django-ckeditor
```
Adicionar *ckeditor* nos *INSTALLED_APPS* em `settings.py`:
```python
INSTALLED_APPS = [
    'ckeditor',
]
```
Em `models.py`, usa-se ``RichTextField`` adicionar os recursos aos modelos:
```python
from ckeditor.fields import RichTextField

class Text(models.Model):
    content = RichTextField()
```
No template *HTML*, inclua `{{ form.media }}` para ter uma visualização personalizada:
```HTML
<form>
    {{ form.media }}
    {{ form.as_p }}
    <input type="submit"/>
</form>
```

Configurações utilizadas nesta aplicação:
```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
            '/',
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'height': 300,
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}
```
