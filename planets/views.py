from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from planets.models import Planet
from planets.serializer import PlanetSerializer


@extend_schema(tags=["Planets"])
class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    search_fields = ["name"]
    ordering_fields = ["name", "population"]
