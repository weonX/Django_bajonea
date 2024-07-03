from django.urls import path
from .views import Pagina1

urlpatterns = [
    path('', Pagina1, name='Pagina1'),
]