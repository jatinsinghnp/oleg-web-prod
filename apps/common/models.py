from django.db import models
import uuid

# Create your models here.
class TimeStampedUUIDModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
