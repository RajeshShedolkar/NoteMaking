from django.db import models

# Create your models here.
class user_details(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.IntegerField()

    def __unicode__(self):
        return self.username

class NoteMaking(models.Model):
    notes_id =  models.CharField(max_length=50)
    note = models.CharField(max_length=100)

    def __unicode__(self):
        return self.note
