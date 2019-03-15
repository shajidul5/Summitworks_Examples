from rest_framework import serializers
from talk.models import Talk

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('name', 'speaker', 'venue', 'duration')