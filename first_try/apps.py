from django.apps import AppConfig


class FirstTryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_try'
    verbose_name = "Apps for animes"

    def ready(self):
        import first_try.templatetags.custom_filters