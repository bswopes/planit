from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length = 200)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.name

class UserActivity(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)

class Friend(models.Model):
    user1 = models.ForeignKey(User)
    user2 = models.ForeignKey(User)
