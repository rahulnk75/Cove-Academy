from django.urls import path
from . import views

urlpatterns = [
    # start exam categotys
    path('index_page/',views.index_page,name='index_page'),

    path('Exam_Category/',views.Exam_Category,name='Exam_Category'),
    path('Save_Exam_Category,',views.Save_Exam_Category,name='Save_Exam_Category'),
    path('Display_Exam_Category/',views.Display_Exam_Category,name='Display_Exam_Category'),
    path('Delete_Exam_Category/<int:del_id>/',views.Delete_Exam_Category,name='Delete_Exam_Category'),
    path('Edit_Exam_Category/<int:edit_id>/',views.Edit_Exam_Category,name='Edit_Exam_Category'),
    path('Upload_Exam_Category/<int:upd_id>/',views.Upload_Exam_Category,name='Upload_Exam_Category'),
    # end exam categotys

    # start course details
    path('Add_Course/',views.Add_Course,name='Add_Course'),
    path('Save_Course/',views.Save_Course,name='Save_Course'),
    path('Dispaly_Course/',views.Dispaly_Course,name='Dispaly_Course'),
    path('Delete_Course/<int:del_id>/',views.Delete_Course,name='Delete_Course'),
    path('Edit_Course/<int:edit_id>/',views.Edit_Course,name='Edit_Course'),
    path('Upload_Course/<int:upd_id>/',views.Upload_Course,name='Upload_Course'),
    # end course details

    # start subject details
    path('Add_Subject/',views.Add_Subject,name='Add_Subject'),
    path('Save_Subject/',views.Save_Subject,name='Save_Subject'),
    path('Display_Subject/',views.Display_Subject,name='Display_Subject'),
    path('Delete_Subject/<int:sub_id>/',views.Delete_Subject,name='Delete_Subject'),
    path('Edit_Subject/<int:edit_id>/',views.Edit_Subject,name='Edit_Subject'),
    path('Update_Subject/<int:upd_id>/',views.Update_Subject,name='Update_Subject'),

    # end subject details

    # login page start
    path('Login_Page/',views.Login_Page,name='Login_Page'),
    path('Admin_Login/',views.Admin_Login,name='Admin_Login'),
    path('Admin_Logout/',views.Admin_Logout,name='Admin_Logout'),
    # login page end

    # start contact details
    path('Contact_display/',views.Contact_display,name='Contact_display'),
    path('Contact_delete/<int:del_id>/',views.Contact_delete,name='Contact_delete')
    # end contact details

]
