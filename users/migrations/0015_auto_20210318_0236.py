# Generated by Django 3.1.7 on 2021-03-18 02:36

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210318_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://drive.google.com/file/d/1lcNeZkK9hQ5loBUHCbscJPetPngTWvD8/view?usp=sharing', upload_to=users.models.uploadImg_to),
        ),
    ]