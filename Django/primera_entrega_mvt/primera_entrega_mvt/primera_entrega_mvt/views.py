from django.http import HttpResponse
import datetime 
from django.template import Template, Context
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def alo(request):
    return HttpResponse ("ya entendimos este :)")

def mi_nombre_es(self, nombre):
    documento_de_texto = f"mi nombre es: {nombre}"

    return HttpResponse(documento_de_texto)






