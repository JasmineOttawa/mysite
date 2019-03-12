import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class mapURL(models.Model):
    sURL = models.CharField(max_length=6)
    lURL = models.CharField(max_length=512)
    created = models.DateTimeField('date created')
    def __str__(self):
        return self.lURL
    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
