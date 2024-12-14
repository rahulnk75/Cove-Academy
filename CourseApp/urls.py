from django.urls import path
from . import views

urlpatterns = [
    path('Courses_Filterd/<Cour_name>/',views.Courses_Filterd,name='Courses_Filterd'),
    path('Subject_Filterd/<sub_name>/',views.Subject_Filterd,name='Subject_Filterd'),
    path('Explore_Course/<int:Ex_id>/',views.Explore_Course,name='Explore_Course'),
    path('All_Classes/',views.All_Classes,name='All_Classes'),
]  