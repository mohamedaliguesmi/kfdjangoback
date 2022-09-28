from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE
# Create your models here.




class role(models.Model):

    ROLE = (
			('Arbitrator', 'Arbitrator'),
			('Athlete', 'Athlete'),
			('Coach', 'Coach'),
            ('Club','Club'),
            ('Supporter','Supporter'),
			)

    
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    roles = models.CharField(max_length=200, null=True, choices=ROLE)


    class Meta:
        ordering = ['created']





class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    


    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    country = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    

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
    id_grade = models.TextField(null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)

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
    


    class Meta:
        ordering = ['created']


