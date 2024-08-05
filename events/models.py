from django.db import models
from django.conf import settings



class Event(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="events_organizer")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="events",blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000,blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255,blank=True,default="Iran,Tehran")

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.organizer} -- {self.title}"