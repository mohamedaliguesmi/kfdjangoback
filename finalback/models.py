from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class role(models.Model):

    ROLE = (
			('Arbitrator', 'Arbitrator'),
			('Athlete', 'Athlete'),
			('Coach', 'Coach'),
            ('Club','Club'),
			)

    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    roles = models.CharField(max_length=200, null=True, choices=ROLE)


    class Meta:
        ordering = ['created']