# Generated by Django 3.0.5 on 2021-02-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210221_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[(' ', ' '), ('Film & Animation', 'Film & Animation'), ('Autos & Vehicles', 'Autos & Vehicles'), ('Music', 'Music'), ('Pets & Animals', 'Pets & Animals'), ('Autos & Vehicles', 'Autos & Vehicles'), ('Sports', 'Sports'), ('Travel & Events', 'Travel & Events'), ('Gaming', 'Gaming'), ('People & Blogs', 'People & Blogs'), ('Comedy', 'Comedy'), ('Entertainment', 'Entertainment'), ('News & Politics', 'News & Politics'), ('Howto & Style', 'Howto & Style'), ('Education', 'Education'), ('Science & Technology', 'Science & Technology'), ('Nonprofits & Activism', 'Nonprofits & Activism')], default=' ', max_length=30),
        ),
    ]
