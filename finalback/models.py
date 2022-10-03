from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE
# Create your models here.




class role(models.Model):



    
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    roles = models.CharField(max_length=200, null=True)


    class Meta:
        ordering = ['created']

class Weights(models.Model):

 
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    masse_en_killograme = models.IntegerField()

    class Meta:
        ordering = ['created']


class Categorie(models.Model):

 
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    categorie_age = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        ordering = ['created']


class Grade(models.Model):

 
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    Grade = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        ordering = ['created']

class Seasons(models.Model):

 
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    Seasons = models.CharField(max_length=200, null=True, blank=True)
    activated =models.BooleanField(default=False)
    


    class Meta:
        ordering = ['created']


class Licences(models.Model):


    user = models.OneToOneField(User, null=True, on_delete=models.DO_NOTHING)
    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.DO_NOTHING)
    seasons =models.ForeignKey(Seasons, null=True, blank=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    num_licences = models.IntegerField(null=True, blank=True)
    activated =models.BooleanField(default=False)


    class Meta:
        ordering = ['created']


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    


    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.DO_NOTHING)
    licences = models.ForeignKey(Licences, null=True, on_delete=models.CASCADE)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    profile_photo = models.ImageField( upload_to='image/', null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    location = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    cin = models.TextField(null=True, blank=True)
    

    class Meta:
        ordering = ['created']




class Club(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    
    

    class Meta:
        ordering = ['created']


class Supporter(models.Model):
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    club = models.OneToOneField(Club, null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    
    
    

    class Meta:
        ordering = ['created']



class Arbitrator(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    cin = models.IntegerField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    sex = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['created']

class Coach(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    cin = models.IntegerField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    sex = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['created']

class Athlete(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    sex = models.TextField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    grade_id = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    id_degree = models.IntegerField(null=True, blank=True)
    cin = models.TextField(null=True, blank=True)
    nationality =models.TextField(null=True, blank=True)
    photo = models.ImageField( upload_to='image/', null=True, blank=True)
    idantity_photo = models.ImageField( upload_to='image/', null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    weights = models.ForeignKey(Weights, null=True, on_delete=models.DO_NOTHING)
    


    class Meta:
        ordering = ['created']


