from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('Nome', max_length=100, blank=False, null=False)
    password = models.CharField('Senha', max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username


class Text(models.Model):
    title = models.CharField('Titulo', max_length=100, blank=False, null=False)
    content = RichTextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Texto'
    
    def __str__(self):
        return self.title
