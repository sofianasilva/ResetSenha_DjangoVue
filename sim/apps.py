from django.apps import AppConfig


class SimConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sim"

class SimConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sim"

    def ready(self):
        import sim.signals