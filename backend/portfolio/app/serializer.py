from rest_framework import serializers
from django.utils.text import Truncator
from .models import Profile, Projects, Skill, Technologies

class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill', 'icon']

class TechnologiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ['name']

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillsSerializers(read_only =True, many=True)
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ["id"]

class ProjectSerializer(serializers.ModelSerializer):
    desc = serializers.SerializerMethodField()
    technologies = TechnologiesSerializers(read_only=True, many=True)
    class Meta:
        model = Projects
        fields = '__all__'
    
    def get_desc(self, obj):
        return Truncator(obj.desc).chars(200)

class SingleProjectSeralizer(serializers.ModelSerializer):
    technologies = TechnologiesSerializers(read_only=True, many=True)
    class Meta:
        model = Projects
        fields = '__all__'