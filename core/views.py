from django.forms import widgets
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from core.models import *
from core.forms import ImageForm
from PIL import Image
import PIL
from django.conf import settings
import urllib.request

# Create your views here.


class MainPage(ListView):
    context_object_name = "images"
    template_name = "index.html"
    context_object_name = "images"
    queryset = Images.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['images'] = Images.objects.all()
        return context


# class AddNewImage(CreateView):
#     model = Images
#     fields = ['link', 'image']
#     success_url = "/"
#     template_name = "upload.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            request.POST

            form.save()
            # Get the current instance object to display in the template

            # urllib.request.urlretrieve(
            #     'https://python-scripts.com/wp-content/uploads/2021/01/guido-van-rossum.jpg',
            #     "gfg.jpg")

            img_obj = form.instance

            if img_obj.image:
                height = img_obj.image.height
                width = img_obj.image.width
                return render(request, 'cut.html', {'form': form, 'img_obj': img_obj, 'height': height,
                                                    'width': width})
            return render(request, 'cut.html')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def resize_image_view(request):
    if request.method == 'POST':
        width = int(request.POST.get('width'))
        height = int(request.POST.get('height'))

        im = request.POST.get("image")

        name = im.replace("images/", "")

        image = Image.open(str(settings.MEDIA_ROOT) + "/" + im)

        height_percent = (height / float(image.size[1]))
        new_width = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((new_width, height), PIL.Image.NEAREST)
        image = image.convert("RGB")
        name = "edited_" + name
        image.save(str(settings.MEDIA_ROOT) + "/edited/" + name)

        return redirect("/")

        # return render(request, 'index.html')
