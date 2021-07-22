
from os import name
from django.urls import path
from core.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", MainPage.as_view(), name="main_page_link"),
    path("add/", image_upload_view, name="add_image_link"),
    path("resize/", resize_image_view, name="resize_image_link")
]
