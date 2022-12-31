from django.db import models
from django.utils import timezone
import json

# Create your models here.
def resumePath(obj, filename):
    return f"uploads/resume/{filename}"

def iconPath(obj,filename):
    return f"uploads/icons/{obj.skill}_{filename}"

def imagePath(obj, filename):
    return f"uploads/images/{obj.title}_{filename}"

def screenshotPath(obj, filename):
    return f"uploads/screenshots/{obj.project.title}/{filename}"


class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to=resumePath, null=True, blank=True)
    updated_on = models.DateTimeField(default= timezone.now)
    # skills = models.ManyToManyField(Skill)
    def __str__(self):
        return str(self.name)

class Skill(models.Model):
    skill = models.CharField(max_length=100, null=True, blank=True)
    icon = models.FileField(upload_to=iconPath, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    def __str__(self):
        return str(f"{self.skill} : {self.icon.url if self.icon else None}")


class Projects(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    img = models.FileField(upload_to=imagePath)
    # technologies = models.ManyToManyField(Technologies)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    is_present = models.BooleanField(default=True)
    # screenshots = models.ManyToManyField(Screenshots)
    git_repo = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.title)

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='technologies', null=True, blank=True)
    def __str__(self):
        return str(self.name)

class Screenshots(models.Model):
    img = models.ImageField(upload_to=screenshotPath)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='screenshots', null=True, blank=True)
    def __str__(self):
        return str(self.img.url)

class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    whatsapp_no = models.CharField(max_length=500, null=True, blank=True)
    insta = models.CharField(max_length=500, null=True, blank=True)
    profile = models.ForeignKey(Profile, related_name='contacts', null=True, blank=True, on_delete=models.CASCADE)