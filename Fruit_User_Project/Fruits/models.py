from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100,unique=True)
    cost = models.IntegerField()
    user_liking = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name+" "+str(self.cost)