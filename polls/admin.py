from django.contrib import admin

# Se registra la aplicación en el sitio administrativo
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)