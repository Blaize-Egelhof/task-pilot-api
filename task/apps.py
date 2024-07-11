from django.apps import AppConfig


class TaskConfig(AppConfig):
    """
    AppConfig class for the 'task' app.

    This class defines configuration settings for the 'task' app,
    including the default database field type and the app name.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task'
