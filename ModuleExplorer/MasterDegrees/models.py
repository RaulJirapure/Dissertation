from django.db import models

# Create your models here.


class Modules(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20)
    description = models.TextField()
    short_description = models.TextField()
    image= models.CharField(max_length=200)
    credits= models.IntegerField(default=10)

    def __str__(self):
        return self.title


class MasterDegrees(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=200)
    description = models.TextField()
    modules = models.ManyToManyField(Modules, help_text='modules for masters')
    short_description = models.TextField()
    image= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    def __str__(self):
        return self.title
    


# Assigning the fields for our Database Models