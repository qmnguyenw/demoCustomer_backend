from django.db import models

# create model and its attributes
class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=1)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name