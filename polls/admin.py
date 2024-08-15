from django.contrib import admin

# Se registra la aplicación en el sitio administrativo
from .models import Question

admin.site.register(Question)