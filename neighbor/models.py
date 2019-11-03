from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    locations = (
        ('Kigali', 'Kimironko'),
        ('Kigali', 'Kacyiru'),
        ('Kigali', 'Kicukiro'),
        ('Kigali', 'Kimihurura'),
        ('Kigali', 'Gacuriro'),
        ('Kigali', 'Nyamirambo'),
        ('Kigali', 'Gikondo'),
        ('Kigali', 'Kiyovu'),
        ('Kigali', 'Kanombe'),
        ('Kigali', 'Kibagabaga'),
        ('Kigali', 'Gisozi'),
              
    )
    name = models.CharField(max_length=65, choices=locations)



    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


    def __str__(self):
        return self.name


class Hood(models.Model):
    name = models.CharField(max_length=50)
    occupants = models.CharField(max_length=50)
    location = models.ForeignKey(Location)
    





class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length = 255,null = True)
    full_name = models.CharField(max_length=255, null=True)
    hood = models.ForeignKey(Hood,null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()



    
