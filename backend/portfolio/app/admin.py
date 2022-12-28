from django.contrib import admin
from .models import Skill, Profile, Projects, Screenshots, Technologies

# Register your models here.

admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Screenshots)
admin.site.register(Technologies)