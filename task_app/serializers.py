from rest_framework import serializers

from .models import Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "age"]
        read_only_fields = ["id"]


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source="user", queryset=User.objects.all()
    )

    class Meta:
        model = Task
        fields = ["id", "user_id", "title", "description", "status"]
        read_only_fields = ["id"]
