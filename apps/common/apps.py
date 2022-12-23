from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):

    """
    this  is common app configutations for sharing common things like data base exception and etc
    all other app is depended in this models
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
    verbose_name: str = _("Common")
