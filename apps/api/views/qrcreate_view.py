from ...social.models import Qrcode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...api.serializers.sociallinkserilizers import QrSerilizer, UserSocialLinks
from ...profiles.models import Profile
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ObjectDoesNotExist


class QrCodeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QrSerilizer

    @swagger_auto_schema(responses={200: QrSerilizer(many=True)})
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user.id)
            qr = Qrcode.objects.get(userprofile=profile)
        except ObjectDoesNotExist:
            return Response({"error":"you dont't have any data "})
        serilizer = self.serializer_class(qr)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=QrSerilizer)
    def post(self, request):
        serilizer = self.serializer_class(data=request.data)
        try:
            qruser = UserSocialLinks.objects.filter(userprofile=request.user.id)
            currentuser = request.user.id
            qruser = qruser[0].userprofile.id
        except:
            return Response(
                {"error": "you need to have at leat one user socail link  "},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if currentuser == qruser:
            if serilizer.is_valid():
                serilizer.save()
                return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"msg": "user id do't match"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


QrCodeView = QrCodeView.as_view()
