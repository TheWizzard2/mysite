from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from polls.models import Question

def index(request):
    # Capturar los datos desde el modelo objetos
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # El contexto es un diccionario que asigna nombres 
    # de variables de plantilla a objetos de Python.
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)