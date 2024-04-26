from rest_framework import serializers

from api.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
    
    source = serializers.CharField(source='source_name')
    # foo = serializers.CharField(source='source_name')