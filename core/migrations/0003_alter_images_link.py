# Generated by Django 3.2.5 on 2021-07-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_images_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='link',
            field=models.CharField(default='', max_length=255, verbose_name='Link'),
        ),
    ]
