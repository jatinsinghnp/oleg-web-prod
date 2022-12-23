from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConnectionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.connections"
    verbose_name: str = _("Connections")
