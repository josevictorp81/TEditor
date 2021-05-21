from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

class Text(models.Model):
    title = models.CharField('Titulo', max_length=100, blank=False, null=False)
    content = RichTextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Texto'
    
    def __str__(self):
        return self.title
