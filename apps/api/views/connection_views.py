from ...connections.models import Connections
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ...api.serializers.connections_serilizer import ConnectionSerilizer
from rest_framework.response import Response
from ...profiles.models import Profile
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class ConnectionView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ConnectionSerilizer(many=True)})
    def get(self, request):
        profilename = Profile.objects.get(user=request.user)
        connections = Connections.objects.filter(profile=profilename)
        serilizer = ConnectionSerilizer(connections, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ConnectionSerilizer)
    def post(self, request):
        serilizer = ConnectionSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


ConnectionView = ConnectionView.as_view()
