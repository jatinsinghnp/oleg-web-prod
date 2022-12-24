from django.db import models
from ..common.models import TimeStampedUUIDModel
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from ..profiles.models import Profile

# Create your models here.
class Connections(TimeStampedUUIDModel):
    profile = models.ForeignKey(
        Profile, related_name="connection_profile", on_delete=models.CASCADE
    )
    peroson_name = models.CharField(max_length=500)
    Email = models.EmailField(blank=True,null=True)
    phone_number = PhoneNumberField(blank=True,null=True)
    job_title = models.CharField(max_length=200, blank=True,null=True)
    company_name = models.CharField(max_length=200,blank=True,null=True)
    Add_note = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.peroson_name
