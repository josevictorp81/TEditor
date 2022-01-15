# TEditor

TEditor é um editor de texto Rich Text, que dispõe de varias opções para a formatação de textos no geral. Para esta aplicação, o usuário deve criar um conta para acessar as opções de: criar, listar, editar e deletar um texto. Possuindo também uma opção para o download do texto em formato PDF.

## Bibliotecas
- [Django](https://www.djangoproject.com/)
- [django-easy-pdf](https://django-easy-pdf.readthedocs.io/en/develop/), renderiza tempaltes em PDFs.
- [Django widgets_tweaks](https://pypi.org/project/django-widget-tweaks/), biblioteca que renderiza campos de formulário em templates.
- [Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/), biblioteca que integra um editor do tipo "WYSIWYG".

### Django CKEditor

Configurações personalizadas utilizadas no CKEditor:
`Settings.py`:
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
