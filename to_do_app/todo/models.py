from django.db import models
from datetime import datetime, date, timezone
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False)
    end_date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField()
    
    @property
    def is_outdated(self):
        now = datetime.now(timezone.utc)
        if now > self.end_date and self.status == False:
                return True
        return False
