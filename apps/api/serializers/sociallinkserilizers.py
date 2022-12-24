from apps.social.models import SocialLinks, UserSocialLinks, Qrcode
from rest_framework.serializers import ModelSerializer


class SocialLinksSerilizer(ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"
        depth = 1


class UserSociallinkSerilizer(ModelSerializer):
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
