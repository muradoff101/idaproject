from django.db import models
from django.utils.html import mark_safe
import os
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.files import File
# Create your models here.


class Images(models.Model):
    link = models.URLField("Link", blank=True, default="")
    image = models.ImageField("Image", upload_to="images/", blank=True)
    added_date = models.DateField("", auto_now_add=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = 'Images'

    def get_image(self):
        return mark_safe('<img src="%s" width="350" height="150" />' % (self.image.url))
    get_image.short_description = 'Image'

    def __str__(self) -> str:
        return str(self.pk)

    def get_image_name(self):
        return os.path.basename(self.image.name)

    def save(self, *args, **kwargs):
        if self.link and not self.image:
            # os.environ["PYTHONHTTPSVERIFY"] = "0"
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.link).read())
            img_temp.flush()
            self.image.save(f"image_{self.pk}.jpg", File(img_temp))
        super(Images, self).save(*args, **kwargs)
