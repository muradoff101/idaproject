# Generated by Django 3.2.5 on 2021-07-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_images_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Image'),
        ),
    ]