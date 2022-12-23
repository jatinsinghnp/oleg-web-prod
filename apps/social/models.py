from django.db import models
from ..common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from ..profiles.models import Profile
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class SocialLinks(TimeStampedUUIDModel):
    name = models.CharField(max_length=200, unique=True)
    social_links_images = models.ImageField(default="/links.png")

    def __str__(self) -> str:
        return f"{self.name}"


class UserSocialLinks(TimeStampedUUIDModel):
    userprofile = models.ForeignKey(
        Profile, verbose_name=_("userprofile"), on_delete=models.CASCADE
    )
    sociallinks = models.ForeignKey(
        SocialLinks, verbose_name=_("social_link"), on_delete=models.CASCADE
    )
    profile_links = models.URLField(max_length=200, default=None)

    def __str__(self) -> str:
        return f"{self.sociallinks.name}"


class Qrcode(TimeStampedUUIDModel):
    usersociallink = models.OneToOneField(
        UserSocialLinks, verbose_name=_("usersociallink"), on_delete=models.CASCADE
    )
    profile_qr = models.ImageField(
        _("QR"), upload_to="qr/", default="user.png", blank=True
    )
    userprofile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.usersociallink.userprofile}"

    def save(self, *args, **kwargs):
        if self.usersociallink is not None:
            qr_img = qrcode.make(self.usersociallink.profile_links)
            canvas = Image.new("RGB", (400, 400), "white")
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qr_img)
            link = f'qr_img-{self.usersociallink}" + ".png'
            buffer = BytesIO()
            canvas.save(buffer, "PNG")
            self.profile_qr.save(link, File(buffer), save=False)
            canvas.close()
        else:
            print(self.usersociallink)
        super(Qrcode, self).save(*args, **kwargs)
