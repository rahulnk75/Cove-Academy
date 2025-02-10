from django.db.models.signals import post_save
from django.dispatch import receiver
from StudentsApp.models import ChatGroup, Register_Db
from CourseApp.models import Payment_DB


@receiver(post_save, sender=Payment_DB)
def create_chat_group(sender, instance, created, **kwargs):
    if created:
        course_name = instance.Course_Name.strip()  # Remove spaces
        chat_group, group_created = ChatGroup.objects.get_or_create(course_name=course_name)
        
        if group_created:
            print(f"✅ Chat group created for {course_name}")
        else:
            print(f"⚠️ Chat group already exists for {course_name}")

        # Add student to the group
        student = Register_Db.objects.filter(Full_Name=instance.Full_Name, User_Email=instance.Email).first()
        if student:
            chat_group.members.add(student)
            print(f"✅ {student.Full_Name} added to {course_name} group")
        else:
            print(f"⚠️ No student found for {instance.Full_Name} ({instance.Email})")
