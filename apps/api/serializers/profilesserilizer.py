from ...profiles.models import Profile
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from ...api.serializers.sociallinkserilizers import UserSociallinkSerilizer


class ProfileSerilizer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UpdateProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["gender", "bio", "picture", "name"]
       
