from rest_framework.routers import DefaultRouter

from planets.views import PlanetViewSet

app_name = "planets"

planets_router = DefaultRouter()
planets_router.register(r"planets", PlanetViewSet, basename="api-planets")

urlpatterns = planets_router.urls
