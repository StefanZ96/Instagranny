from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from django_resized import ResizedImageField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(100)
    profileimg = ResizedImageField(size=[360,360] ,blank=True, default="default.profilepic.jpg", upload_to="profile_photos")
    followers = models.ManyToManyField(User, blank=True, related_name = "followers")
    
    @property
    def profileimg_url(self):
        if self.profileimg and hasattr(self.profileimg, 'url'):
            return self.profileimg.url
        else:
            pass
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "creator")
    photo = models.ImageField(blank = True, null=True, upload_to="post_photos")
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name = "posts")
    
    
    def __str__(self):
        return str(self.pk)
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/default_profilepic.jpg"
        
   
    
class Comments(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "comments")
    comm_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.pk)