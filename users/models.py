from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class UserProfile(models.Model):
    id = models.CharField(max_length=18, primary_key=True, editable=False, unique=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    country = models.CharField(max_length=30, blank=False)
    profile_pic = models.ImageField(upload_to='Users-Dps/', default='default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)

        if dp.height > 320 and dp.width > 320:
            output_size = (320, 320)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)

    
class Tasks(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, editable=False)
    task = models.CharField(max_length=30, blank=False)
    subtitle = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.user}'

    