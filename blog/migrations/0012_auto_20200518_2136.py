# Generated by Django 3.0.5 on 2020-05-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200518_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='imagePost_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('POST', 'Post'), ('VID', 'Video'), ('IMG', 'Image')], default='POST', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='video_path',
            field=models.FileField(blank=True, default=None, upload_to='videoPost_vids'),
        ),
    ]
