from django.db import models


# Create your models here.
# create the table
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()

    def __str__(self):
        return self.name  # Return the name of the employee for better readability in admin interface