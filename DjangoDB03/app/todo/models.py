from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.completed)
     