# Generated by Django 3.0.5 on 2020-05-19 06:50

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200518_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=blog.models.uploadImg_to),
        ),
    ]
