from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('text/', views.simple_hello, name='simple_hello'),
    path('api/', views.json_data, name='json_data'),
]