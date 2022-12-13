from rest_framework import serializers
from .models import Profile, Projects, Skill

class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill', 'icon']

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillsSerializers(read_only =True, many=True)
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ["id"]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ["pk"]