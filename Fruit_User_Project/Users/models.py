from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    liked_fruits = models.TextField(blank=True,null=True)
    disliked_fruits = models.TextField(blank=True,null=True)
    not_sure_fruits = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.first_name+" "+self.last_name
    