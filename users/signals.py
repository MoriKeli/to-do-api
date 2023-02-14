from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Tasks
import uuid


@reciever(pre_save, sender=User)
def generate_userProfile_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(pre_save, sender=Tasks)
def generate_task_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            UserProfile.objects.create(name=instance)