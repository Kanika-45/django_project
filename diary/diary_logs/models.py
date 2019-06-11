from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Log(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now_add=True)
    day = models.DateField()
