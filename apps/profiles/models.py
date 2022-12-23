from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ..common.models import TimeStampedUUIDModel

User = get_user_model()

# Create your models here.
class Profile(TimeStampedUUIDModel):
    class Genders(models.TextChoices):
        NONE = "None"
        OTHERS = "Others"
        MALE = "Male"
        FEMALE = "Female"

    user = models.OneToOneField(User, related_name="profiles", on_delete=models.CASCADE)
    bio = models.TextField(default="")
    gender = models.CharField(
        default=Genders.NONE, choices=Genders.choices, max_length=10
    )
    picture = models.ImageField(
        default="/profile_default.png", upload_to="picture", blank=True
    )
    name = models.CharField(max_length=500, blank=True)
   
    

    def __str__(self) -> str:
        return f"{self.user.email}"

    