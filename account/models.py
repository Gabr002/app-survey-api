from django.db import models
from django.utils import timezone

# Create your models here.
class Survey(models.Model): 
    number = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.description