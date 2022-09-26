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
    id = models.IntegerField(primary_key=True)
    roles = models.CharField(max_length=200, null=True, choices=ROLE)


    class Meta:
        ordering = ['created']





class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    


    role =models.OneToOneField(role, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    country = models.TextField()
    state = models.TextField()
    city = models.TextField()
    address = models.TextField()
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=200, null=True)
    location = models.TextField()
    

    class Meta:
        ordering = ['created']




class Club(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    
    

    class Meta:
        ordering = ['created']


class Supporter(models.Model):
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    club = models.OneToOneField(Club, null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    
    
    

    class Meta:
        ordering = ['created']



class Arbitrator(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    cin = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    sex = models.TextField()
    birthday = models.DateField()
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['created']

class Coach(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    cin = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    sex = models.TextField()
    birthday = models.DateField()
    id_grade = models.TextField()
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Athlete(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    sex = models.TextField()
    category_id = models.IntegerField()
    grade_id = models.IntegerField()
    birthday = models.DateField()
    id_degree = models.IntegerField()
    cin = models.TextField(null=True, blank=True)
    nationality =models.TextField()
    photo = models.ImageField( upload_to='image/', null=True, blank=True)
    idantity_photo = models.ImageField( upload_to='image/', null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    


    class Meta:
        ordering = ['created']


