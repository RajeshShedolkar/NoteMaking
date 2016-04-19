from django.db import models

# Create your models here.
class user_details(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.IntegerField()

    def __unicode__(self):
        return self.username
