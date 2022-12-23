from rest_framework.views import APIView
from apps.api.serializers.sociallinkserilizers import (
    UserSociallinkSerilizer,
    UserSocialLinks,
    SocialLinks,
    SocialLinksSerilizer,
)
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView


class SocialView(APIView):
    @swagger_auto_schema(responses={200: SocialLinksSerilizer(many=True)})
    def get(self, request):
        socail_link = SocialLinks.objects.all()
        serilizer = SocialLinksSerilizer(socail_link, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


SocialView = SocialView.as_view()


class UserSocialView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: UserSociallinkSerilizer})
    def get(self, request):
        user_social_link = UserSocialLinks.objects.filter(userprofile=request.user.id)
        serilizer = UserSociallinkSerilizer(user_social_link, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserSociallinkSerilizer)
    def post(self, request):
        serlizer = UserSociallinkSerilizer(data=request.data)
        currentprofileid = request.user.id
        profile_id = UserSocialLinks.objects.filter(userprofile=request.user.id)
        profile_id = profile_id[0].userprofile.id

        if currentprofileid == profile_id:
            if serlizer.is_valid():
                serlizer.save()
                return Response({"msg": "done!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"msg": "user id not found"}, status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serlizer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=UserSociallinkSerilizer)
    def delete(self, request, id):
        try:

            usersocialLinks = UserSocialLinks.objects.filter(pk=id)
            usersocialLinks.delete()
        except Exception as e:
            print(e)

        user_social_link = UserSocialLinks.objects.filter(userprofile=request.user.id)
        serilizer = UserSociallinkSerilizer(user_social_link, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


UserSocialView = UserSocialView.as_view()


class UserSocialLinkUpdate(UpdateAPIView):
    queryset = UserSocialLinks.objects.all()
    serializer_class = UserSociallinkSerilizer
    lookup_field = "id"

    def perform_update(self, serializer):
        return super().perform_update(serializer)


UserSocialLinkUpdate = UserSocialLinkUpdate.as_view()
