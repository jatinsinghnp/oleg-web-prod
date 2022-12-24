from ..serializers.profilesserilizer import ProfileSerilizer, UpdateProfileSerializer
from ...profiles.models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from ...social.models import SocialLinks, UserSocialLinks, Qrcode
from drf_yasg.utils import swagger_auto_schema
from ...api.serializers.sociallinkserilizers import UserSociallinkSerilizer, QrSerilizerprofile


class ProfilePageView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: ProfileSerilizer(many=True)})
    def get(self, request):
        profile = Profile.objects.get(user=request.user.id)
        usersocial = UserSocialLinks.objects.filter(userprofile=profile)
        defualtqr = Qrcode.objects.get(userprofile=profile)
        defaultqrserilizer = QrSerilizerprofile(defualtqr,context={"request": request})
        usersocialserilizer = UserSociallinkSerilizer(usersocial, many=True)
        serilizer = ProfileSerilizer(profile, context={"request": request})
        return Response(
            {
                "profile": serilizer.data,
                "userlink": usersocialserilizer.data,
                "qr": defaultqrserilizer.data,
            },
            status=status.HTTP_200_OK,
        )


ProfilePageView = ProfilePageView.as_view()


class UpdateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.select_related("user")
    serializer_class = UpdateProfileSerializer
    @swagger_auto_schema(
        operation_description="updateprofile", responses={200: UpdateProfileSerializer}
    )
    def patch(self, request, user_email):
        try:
            self.queryset.get(user__email=user_email)
        except Profile.DoesNotExist:
            raise NotFound("this is not your profile")

        user_mail = request.user.email
        if user_mail != user_email:
            return Response(
                {"msg": "you are not authorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profiles, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


UpdateProfileAPIView = UpdateProfileAPIView.as_view()
