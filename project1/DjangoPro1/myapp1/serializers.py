from rest_framework import serializers
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        # Include the owner information while creating the project
        validated_data['owner'] = self.context['request'].user.profile
        return super().create(validated_data)

"""
class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'
"""