from django.urls import path 
from . import views

urlpatterns = [
    path('Meander_login/',views.Meander_login,name='Meander_login')
]
