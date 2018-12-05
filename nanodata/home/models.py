from django.db import models

class TeamMember(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, blank=True)
    nickname =  models.CharField(max_length=200, blank=True)
    biography = models.TextField(default = '', max_length=2000, blank=True)
    picture = models.ImageField(upload_to='home/static/home/images', blank=True)

    def __str__(self):
        return self.firstname
