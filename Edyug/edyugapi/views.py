from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from edyugapi.serializers import PeopleSerializer
from edyugapi.models import People


class PeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer