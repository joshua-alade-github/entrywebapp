# Generated by Django 3.0.5 on 2021-02-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210215_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
    ]