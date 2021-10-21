from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from PIL import Image
from django.db.models import Max

def uploadImg_to(instance, filename):
    return 'images/%s/%s' % (instance.username, filename)

# class PostLikes(models.Model):
#     class Meta:
#         db_table = 'users_profile_liked_posts'
#         # or whatever your table is called
#     post = models.ForeignKey(Post)
#     Profile = models.ForeignKey(profile)
#     liked = models.DateTimeField(null=True, blank=True, auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    image = models.ImageField(blank=True, default='images/default.jpg', upload_to=uploadImg_to)
    name = models.CharField(blank=True, max_length=255)
    #following = models.ManyToManyField(User, related_name='following', blank=True)
    #followers = models.ManyToManyField(User, related_name='followers', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank = True, max_length=250)
    location = models.CharField(blank=True, max_length=40)
    about = models.TextField(blank = True, max_length=1000)
    birth_date = models.DateField(blank=True, null=True)
    occupation = models.CharField(blank=True, max_length=100)
    liked_posts = models.ManyToManyField(Post, related_name='user_liked_posts', blank=True)
    view_later = models.ManyToManyField(Post, related_name='user_view_later_posts', blank=True)
    #liked_posts = models.ManyToManyField(Post, through='PostLikes', related_name='user_liked_posts', blank=True)


    #@property
    #def followers():
    #    return Follow.objects.filter(follow_user=self.user).count()

    #@property
    #def following():
    #    return Follow.objects.filter(user=self.user).count()

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.created = self.user.date_joined
        self.username = self.user.username

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def profiles_posts(self):
        return self.user.post_set.all()

    def __str__(self):
        return f'{self.user.username} Profile'

    # def total_followers(self):
    #     return self.followers.count()
    #
    # def total_following(self):
    #     return self.following.count()

    class Meta:
        ordering = ('-created',)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
#
#     def __str__(self):
#         return '{} follows {}'.format(self.user_from, self.user_to)
#
# User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
	body = models.TextField(max_length=1000, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def send_message(from_user, to_user, body):
		sender_message = Message(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			is_read=True)
		sender_message.save()

		recipient_message = Message(
			user=to_user,
			sender=from_user,
			body=body,
			recipient=from_user,)
		recipient_message.save()
		return sender_message

	def get_messages(user):
		messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': User.objects.get(pk=message['recipient']),
				'last': message['last'],
				'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users
