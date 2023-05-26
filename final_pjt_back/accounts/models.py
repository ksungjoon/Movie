from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.ImageField(blank=True, upload_to='profile_image')
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None