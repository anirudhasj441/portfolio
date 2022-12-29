from django.contrib import admin
from .models import Skill, Profile, Projects, Screenshots, Technologies

# Register your models here.
class ScreenshotInLine(admin.StackedInline):
    model = Screenshots

class TechnologiesInLine(admin.StackedInline):
    model = Technologies

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ScreenshotInLine,
        TechnologiesInLine
    ]
    class Media:
        js = ('app/js/inject_tiny.js',)

admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Screenshots)
admin.site.register(Technologies)