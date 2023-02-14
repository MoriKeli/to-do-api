from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Tasks
import uuid


@receiver(pre_save, sender=UserProfile)
def generate_userProfile_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(pre_save, sender=Tasks)
def generate_task_ID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]
