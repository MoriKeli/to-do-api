from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Tasks
import uuid

@receiver(pre_save, sender=Tasks)
def generate_tasksID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:10]
