from rest_framework import serializers
from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    """
    To serialize the Info Model into JSON format
    """

    class Meta:
        model = Info
        fields = (
            'slack_name',
            'track',
            'github_username',
            'github_repo',
            'github_file'
        )