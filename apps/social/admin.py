from django.contrib import admin
from .models import SocialLinks, UserSocialLinks,Qrcode

# Register your models here.

admin.site.register(SocialLinks)
admin.site.register(UserSocialLinks)
admin.site.register(Qrcode)
