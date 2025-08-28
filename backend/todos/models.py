from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return self.title