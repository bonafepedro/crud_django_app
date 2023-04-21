from django.apps import AppConfig


class AppcargasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appcargas'

    def ready(self):
        import appcargas.signals
