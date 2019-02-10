from django.contrib.auth.models import User, Group
from rest_framework import serializers
from edyugapi.models import People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'fname', 'lastname')



