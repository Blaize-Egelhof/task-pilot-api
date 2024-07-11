from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    AppConfig class for the 'profiles' app.

    This class defines configuration settings for the 'profiles' app,
    including the default database field type and the app name.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
