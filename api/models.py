from django.db import models

# Create your models here.
class Test(models.Model):
    # notes_id = models.ForeignKey(Notes)
    test_id = models.CharField(max_length=50)
    note = models.CharField(max_length=100)

    def __unicode__(self):
        return self.note

