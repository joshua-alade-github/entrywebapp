# Generated by Django 3.0.5 on 2020-05-04 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200504_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='bodyy',
        ),
    ]
