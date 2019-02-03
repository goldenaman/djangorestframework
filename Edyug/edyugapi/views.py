from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Edyug.edyugapi.serializers import PeopleSerializer
from Edyug.edyugapi.models import People


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