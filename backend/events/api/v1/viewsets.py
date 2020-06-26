from rest_framework import authentication
from events.models import Events
from .serializers import EventsSerializer
from rest_framework import viewsets


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Events.objects.all()
