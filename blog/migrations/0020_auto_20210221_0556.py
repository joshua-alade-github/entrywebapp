# Generated by Django 3.0.5 on 2021-02-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210215_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('', ''), ('Film & Animation', 'Film & Animation'), ('Autos & Vehicles', 'Autos & Vehicles'), ('Music', 'Music'), ('Pets & Animals', 'Pets & Animals'), ('Autos & Vehicles', 'Autos & Vehicles'), ('Sports', 'Sports'), ('Travel & Events', 'Travel & Events'), ('Gaming', 'Gaming'), ('People & Blogs', 'People & Blogs'), ('Comedy', 'Comedy'), ('Entertainment', 'Entertainment'), ('News & Politics', 'News & Politics'), ('Howto & Style', 'Howto & Style'), ('Education', 'Education'), ('Science & Technology', 'Science & Technology'), ('Nonprofits & Activism', 'Nonprofits & Activism')], default=' ', max_length=30),
        ),
    ]