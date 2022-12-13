from django.db import models
from django.utils import timezone

# Create your models here.
def resumePath(obj, filename):
    return f"uploads/resume/{filename}"

def iconPath(obj,filename):
    return f"uploads/icons/{obj.skill}_{filename}"

def imagePath(obj, filename):
    return f"uploads/images/{obj.title}_{filename}"

class Skill(models.Model):
    skill = models.CharField(max_length=100, null=True, blank=True)
    icon = models.FileField(upload_to=iconPath, null=True, blank=True)
    def __str__(self):
        return str(self.skill)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to=resumePath, null=True, blank=True)
    updated_on = models.DateTimeField(default= timezone.now)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return str(self.name)

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Projects(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    img = models.FileField()
    technologies = models.ManyToManyField(Technologies)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    is_present = models.BooleanField(default=True)
    def __str__(self):
        return str(self.title)
