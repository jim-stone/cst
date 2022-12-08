from django.apps import AppConfig


class SlownikiConfig(AppConfig):
    name = 'slowniki'

    def ready(self):
        import slowniki.signals