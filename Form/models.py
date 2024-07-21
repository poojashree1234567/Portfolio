from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(to  = User, on_delete = models.CASCADE)

    DEGREE_CHOICE =[
        ('1', 'Masters'),
        ('2', 'Under Graduate'),
        ('3', 'Graduate'),
        ('4', 'Diploma'),
    ]
    FREELANCE =[
        ('1', 'Avalaible'),
        ('2', 'Not avalaible'),
    ]
    profile_image = models.ImageField(upload_to='porfile', null=True, blank=True)
    timeline_image = models.ImageField(upload_to='timeline', null=True, blank=True)
    profession = models.CharField(max_length=200, null=True, blank=True)
    thread_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkdin_url = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    degree = models.CharField(max_length=30, choices=DEGREE_CHOICE, null=True, blank=True)
    country_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    address = models.TextField(max_length=100, null=True, blank=True)
    freelance = models.CharField(max_length=20, choices=FREELANCE, null=True, blank=True)
    happy_client = models.IntegerField(null=True, blank=True)
    projects = models.IntegerField(null=True, blank=True)
    hr_of_support =  models.IntegerField(null=True, blank=True)
    hard_work = models.IntegerField(null=True, blank=True)
    i_agree = models.BooleanField(default=True, null=True, blank=True)

class skill(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE)
    skill_name = models.CharField(max_length=200)
    skill_percentage = models.IntegerField()
