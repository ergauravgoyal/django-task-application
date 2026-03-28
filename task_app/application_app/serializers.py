from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id",
            "job",
            "applicant_name",
            "applicant_email",
            "applicant_status",
            "created_at",
        ]
        read_only_fields = ["created_at"]
