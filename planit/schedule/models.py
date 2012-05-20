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
    #user = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 200)
    activities = models.ManyToManyField(Activity)

    def __unicode__(self):
        return self.name

#class UserActivity(models.Model):
    #user = models.ForeignKey(User, related_name='activities')
    #activity = models.ForeignKey(Activity, related_name='users')
