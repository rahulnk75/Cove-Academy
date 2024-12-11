from django.urls import path
from . import views

urlpatterns = [
    path('Home_Page/',views.Home_Page,name='Home_Page'),
    path('About_Page/',views.About_Page,name='About_Page'),
    path('Contact_Page/',views.Contact_Page,name='Contact_Page'),
    path('Save_Contact/',views.Save_Contact,name='Save_Contact'),
    path('Courses_Filterd/<Cour_name>/',views.Courses_Filterd,name='Courses_Filterd'),
    path('Course_Page/',views.Course_Page,name='Course_Page'),
    path('Subject_Page/',views.Subject_Page,name='Subject_Page'),
    path('Subject_Filterd/<sub_name>/',views.Subject_Filterd,name='Subject_Filterd'),
    path('All_login_page/',views.All_login_page,name='All_login_page'),
    path('Textbook_Page/',views.Textbook_Page,name='Textbook_Page'),
    path('Blog_page/',views.Blog_page,name='Blog_page')
] 