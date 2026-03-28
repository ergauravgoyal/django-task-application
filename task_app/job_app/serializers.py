from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "jobs"
        model = Job
        fields = ["id", "title", "company", "location", "description", "created_at"]
        read_only_fields = ["id", "created_at"]
