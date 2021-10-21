from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

def uploadImg_to(instance, filename):
    return 'images/%s/%s' % (instance.author.username, filename)

def uploadVid_to(instance, filename):
    return 'videos/%s/%s' % (instance.author.username, filename)

class Category(models.Model):
    name = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    POST = "POST"
    VID = "VID"
    IMG = "IMG"

    POST_TYPES = (
        (POST, "Post"),
        (VID, "Video"),
        (IMG, "Image"),
    )

    CATEGORY_TYPES = (
        (' ', " "),
        ('Film & Animation', "Film & Animation"),
        ('Autos & Vehicles', "Autos & Vehicles"),
        ('Music', "Music"),
        ('Pets & Animals', "Pets & Animals"),
        ('Autos & Vehicles', "Autos & Vehicles"),
        ('Sports', "Sports"),
        ('Travel & Events', "Travel & Events"),
        ('Gaming', "Gaming"),
        ('People & Blogs', "People & Blogs"),
        ('Comedy', "Comedy"),
        ('Entertainment', "Entertainment"),
        ('News & Politics', "News & Politics"),
        ('Howto & Style', "Howto & Style"),
        ('Education', "Education"),
        ('Science & Technology', "Science & Technology"),
        ('Nonprofits & Activism', "Nonprofits & Activism"),
    )

    title = models.CharField(default=None, max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    allow_comments = models.BooleanField('allow comments', default=True)
    #content = models.TextField()
    content = RichTextField(blank=True, null=True)
    video_path = models.FileField(blank=True, default=None, upload_to=uploadVid_to)
    # image = models.ImageField(blank=True, default=None, upload_to=uploadImg_to)
    image = models.FileField(blank=True, default=None, null=True, upload_to=uploadImg_to)
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default="POST")
    category = models.CharField(max_length=30, choices=CATEGORY_TYPES, default=" ")
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    #dislikes = models.ManyToManyField(User, related_name='disliked_posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):

        try:
            super(Post, self).save(*args, **kwargs)
            img = Image.open(self.image.path)

            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.image.path)

        except: pass

        try:
            f = open(self.video_path.path)
            self.Post.save(new_name, File(f))
            super(Post, self).save(*args, **kwargs)
        except: pass
