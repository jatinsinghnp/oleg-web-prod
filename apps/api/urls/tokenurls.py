from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from ..views.token_views import UserTokenObtainPairView


urlpatterns = [
    path("login/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
