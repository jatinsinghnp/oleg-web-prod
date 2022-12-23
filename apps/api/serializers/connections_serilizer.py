from ...connections.models import Connections
from rest_framework.serializers import ModelSerializer, StringRelatedField


class ConnectionSerilizer(ModelSerializer):
    class Meta:
        model = Connections
        fields = (
            "profile",
            "peroson_name",
            "Email",
            "phone_number",
            "job_title",
            "company_name",
            "Add_note",
        )
    def to_representation(self, instance):
        rep = super(ConnectionSerilizer, self).to_representation(instance)
        rep["profile"] = instance.profile.name
        return rep

