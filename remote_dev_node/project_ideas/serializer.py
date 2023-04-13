from .models import Idea, Vote
from rest_framework import serializers


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'idea_url', 'status']


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['idea', 'reason']