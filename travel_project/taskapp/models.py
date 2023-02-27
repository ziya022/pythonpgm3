from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.name

class Q(models.Model):
    n=models.CharField(max_length=250)
    i=models.ImageField(upload_to='x')
    d=models.TextField()
    r=models.IntegerField()

    def __str__(self):
        return self.n