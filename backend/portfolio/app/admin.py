from django.contrib import admin
from .models import Skill, Profile, Projects, Technologies

# Register your models here.

admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Technologies)