
from django.urls import path

from administracion.views import administracion
from usuarios.views import usuarios

urlpatterns = [
    path('', administracion,name='administracion'),
    path('',usuarios,name="usuarios"),
    
]