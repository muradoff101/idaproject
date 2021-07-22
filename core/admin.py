from django.contrib import admin
from core.models import Images

# Register your models here.


@admin.register(Images)
class AdminImages(admin.ModelAdmin):
    list_display = ("image", "link")
