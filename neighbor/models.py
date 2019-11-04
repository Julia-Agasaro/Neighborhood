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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)





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



    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls, id):
        post = Post.objects.filter(hood__pk=id)
        return post

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(business_name__icontains=search_term)
        return business


    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(hood__pk=id)
        return business