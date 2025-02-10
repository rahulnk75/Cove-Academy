from django.apps import AppConfig

class StudentsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StudentsApp'

    def ready(self):
        import StudentsApp.signals  # Load signals
