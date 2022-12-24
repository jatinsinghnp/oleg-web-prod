from apps.social.models import SocialLinks, UserSocialLinks, Qrcode
from rest_framework.serializers import ModelSerializer


class SocialLinksSerilizer(ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"

class SocialLinksSerilizerForUserSociallinkSerilizer(ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "name", "social_links_images"]


class UserSociallinkSerilizer(ModelSerializer):
    sociallinks = SocialLinksSerilizerForUserSociallinkSerilizer(read_only=True)

    class Meta:
        model = UserSocialLinks
        fields = ["sociallinks", "userprofile", "profile_links"]


class UpdateUserSocialSerilizer(ModelSerializer):
    class Meta:
        model = UserSocialLinks
        fields = "__all__"


class QrSerilizer(ModelSerializer):
    class Meta:
        model = Qrcode
        fields = ["userprofile", "usersociallink"]


class QrSerilizerprofile(ModelSerializer):
    class Meta:
        model = Qrcode
        fields = ["id","profile_qr","usersociallink","userprofile"]
