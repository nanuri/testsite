from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey ('auth.user')
    title = models.CharField (max_length=200)
    text = models.TextField(max_length=500,blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now) # default=timezone.now
    published_date = models.DateTimeField(blank=True, null=True) # blank=True, null=True

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __title__(self):
        return self.title

