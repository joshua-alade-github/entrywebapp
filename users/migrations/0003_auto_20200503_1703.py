# Generated by Django 3.0.5 on 2020-05-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200403_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]