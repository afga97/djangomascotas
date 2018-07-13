from django.urls import path
from apps.adopcion.views import index_adopcion

app_name = 'adopcion'
urlpatterns = [
    path('index', index_adopcion)
]
