import os
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from common.utility import UPLOADS_DIR

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_text = models.TextField(max_length = 900)
    created = models.DateTimeField(default = now)

    @classmethod
    def oldest_posts(cls):
        return cls.objects.all().order_by('created')

    @classmethod
    def newwest_posts(cls):
        return cls.objects.all().order_by('-created')
    
    @classmethod
    def lastday_posts(cls):
        yesterday = now() - timedelta(days=1)
        return cls.objects.all().filter(created__gte = yesterday).order_by('-created')

    @classmethod
    def all_user_posts(cls, user):
        return cls.objects.all().filter(author__username=user).order_by("-created")

    def __str__(self):
        return str(('{} {}'.format(self.author.username, self.created)))

class PostAttachment(models.Model):
    def get_upload_path(self, filename):
        name, ext = os.path.splitext(filename)
        return os.path.join(UPLOADS_DIR, str(self.post.pk), slugify(name) + ext)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    attachment_img = models.ImageField(upload_to=get_upload_path)