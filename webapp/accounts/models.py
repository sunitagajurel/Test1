from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator

# Create your models here.

class PatientProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	firstName = models.CharField(max_length=20, default='')
	lastName = models.CharField(max_length=20, default='')
	gender = models.CharField(max_length = 1, choices=(('M','Male'),('F','Female')),blank=True)
	age = models.PositiveIntegerField(blank=True, null=False,default=14,validators=[MaxValueValidator(100)])

def create_profile(sender, **kwargs):
	if kwargs['created']:
		Patient_profile = PatientProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender = User)