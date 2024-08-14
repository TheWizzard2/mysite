from django.db import models

# Create your models here.
# Entidad que representa la pregunta de la encuesta
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("fecha publicación")

# Entidad que representa la respuesta o elección del votante
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
