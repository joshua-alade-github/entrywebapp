# Generated by Django 3.0.5 on 2020-05-18 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_imagepost_videopost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videopost',
            name='path',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='allow_comments',
            field=models.BooleanField(default=True, verbose_name='allow comments'),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='caption',
            field=models.TextField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='videopost',
            name='allow_comments',
            field=models.BooleanField(default=True, verbose_name='allow comments'),
        ),
        migrations.AddField(
            model_name='videopost',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='videopost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='videopost',
            name='description',
            field=models.TextField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='videopost',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='videopost',
            name='video_path',
            field=models.FileField(default=None, upload_to='videoPost_vids'),
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(default=None, upload_to='imagePost_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
