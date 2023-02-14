from django.db import models

class Tasks(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    task = models.CharField(max_length=30, blank=False)
    subtitle = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.user}'

    