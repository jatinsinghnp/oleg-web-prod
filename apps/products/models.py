from django.db import models
from ..common.models import TimeStampedUUIDModel

from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProductCatageory(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)
    catageory = models.ForeignKey(ProductCatageory, on_delete=models.CASCADE)
    product_description = models.TextField()
    product_image = models.ImageField(
        default="/default.png",
    )

    def __str__(self) -> str:
        return f"{self.name}"
