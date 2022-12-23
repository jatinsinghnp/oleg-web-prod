from rest_framework.response import Response
from ...products.models import Product
from ...api.serializers.product_serilizer import ProductSerilizer
from rest_framework.generics import ListAPIView

class ProductListApiView(ListAPIView):
    model = Product
    serializer_class = ProductSerilizer
    queryset = Product.objects.all()


ProductListApiView = ProductListApiView.as_view()
