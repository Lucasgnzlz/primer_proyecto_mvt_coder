
from django.contrib import admin
from django.urls import path
from primera_entrega_mvt.views import saludo, alo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundavista/', alo),
]
