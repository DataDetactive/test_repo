from django.db import models

# Create your models here.

class Cast(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Category(models.Model):
    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag

class Country(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField(max_length=255)
    year = models.DateTimeField()
    poster = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    casts = models.ManyToManyField(Cast)
    tags = models.ManyToManyField(Category)
    countries = models.ForeignKey(Country,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

