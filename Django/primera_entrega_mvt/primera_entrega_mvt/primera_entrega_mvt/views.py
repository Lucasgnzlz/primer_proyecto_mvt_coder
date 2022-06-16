from django.http import HttpResponse
import datetime 
from django.template import Template, Context
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")






