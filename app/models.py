from django.db import models
import datetime

# Create your models here.


class Post(models.Model):
    subject = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    note = models.CharField(max_length=300)
    created = models.DateField(default=datetime.datetime.now)
    due = models.DateField(default=datetime.datetime.now)
    complete = models.BooleanField(default=False, null=True)

    @property
    def urgent(self):
        today = datetime.date.today()
        if (self.due - today).days < 2:
            return True
        else:
            return False
        
    def __str__(self):
        return f'{self.user}: {self.note} {self.created} {self.due} complete: {self.complete} urgent: {self.urgent}'
