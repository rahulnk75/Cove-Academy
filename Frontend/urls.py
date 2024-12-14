from django.urls import path
from . import views

urlpatterns = [
    path('Home_Page/',views.Home_Page,name='Home_Page'),
    path('About_Page/',views.About_Page,name='About_Page'),
    path('Contact_Page/',views.Contact_Page,name='Contact_Page'),
    path('Save_Contact/',views.Save_Contact,name='Save_Contact'),
    path('Course_Page/',views.Course_Page,name='Course_Page'),
    path('Subject_Page/',views.Subject_Page,name='Subject_Page'),
    path('Textbook_Page/',views.Textbook_Page,name='Textbook_Page'),
    path('Blog_page/',views.Blog_page,name='Blog_page'),
    path('Payment_Page/<int:pay_id>/',views.Payment_Page,name='Payment_Page'),
]  