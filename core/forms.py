from django import forms
from django.forms import fields, ValidationError
from .models import Images


class ImageForm(forms.ModelForm):

    # link = forms.CharField("Link", required=False, max_length=255)

    class Meta:
        model = Images
        fields = ("link", "image",)

    def clean(self):
        cleaned_data = super().clean()
        link = cleaned_data.get('link')
        image = cleaned_data.get('image')

        if link and image:
            raise ValidationError("Заполните только одно поле!!!")

        return cleaned_data
