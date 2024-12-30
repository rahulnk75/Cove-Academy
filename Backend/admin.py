from django.contrib import admin
from Backend.models import Exam_Db,Course_Db
from MentorsApp.models import Mentors_Register_Db

# Register your models here.
admin.site.register(Exam_Db),
admin.site.register(Course_Db)

class MentorAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'Email', 'Mobile', 'is_approved')
    actions = ['approve_mentor']

    def approve_mentor(self, request, queryset):
        for mentor in queryset:
            mentor.is_approved = True
            mentor.save()

admin.site.register(Mentors_Register_Db, MentorAdmin)

