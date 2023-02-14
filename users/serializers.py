from rest_framework import serializers
from .models import UserProfile, Tasks


class UserProfileSerializer(serializers.ModelSerializer):
    model = UserProfile
    fields = ['gender', 'phone_no', 'country', 'profile_pic']

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'