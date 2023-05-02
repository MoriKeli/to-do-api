from django.db import models


class Tasks(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    task = models.TextField(blank=False)    # scheduled task -> what the user is planning to do
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Tasks'