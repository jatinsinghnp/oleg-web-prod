from django.urls import path
from ..routers import router
from ..views.profile_viewset import UpdateProfileAPIView
from ...api.views.connection_views import ConnectionView
from ...api.views.product_view import ProductListApiView
from ...api.views.profile_viewset import ProfilePageView
from ...api.views.social_views import SocialView, UserSocialView, UserSocialLinkUpdate
from ...api.views.qrcreate_view import QrCodeView

urlpatterns = [
    path(
        "update/<str:user_email>/",
        UpdateProfileAPIView,
        name="profile-update",
    ),
    path(
        "social/",
        SocialView,
        name="social",
    ),
    path(
        "usersocial/",
        UserSocialView,
        name="usersocial",
    ),
    path(
        "usersocial/<int:id>/",
        UserSocialView,
        name="usersocial",
    ),
    path(
        "updateusersocial/update/<int:id>/",
        UserSocialLinkUpdate,
        name="update-api",
    ),
    path(
        "qrcode/",
        QrCodeView,
        name="qr-view",
    ),
    path("connection/", ConnectionView, name="connection-view"),
    path("profile/", ProfilePageView, name="profile-view"),
    path("product/", ProductListApiView, name="product-view"),
] + router.urls
