from ...products.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerilizer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
