from logging import getLogger

import requests
from django.core.management.base import BaseCommand
from django.db import DatabaseError

from planets.models import Planet

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "Fill the database with initial planet data"

    def handle(self, *args, **options):
        try:
            response = requests.get(
                "https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20{allPlanets{planets{name%20population%20terrains%20climates}}}"
            )
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching planet data: {e}")
            self.stdout.write(self.style.ERROR("Failed to fetch planet data"))
            return

        data = response.json()

        for planet_data in (
            data.get("data", {}).get("allPlanets", {}).get("planets", [])
        ):
            try:
                Planet.objects.create(
                    name=planet_data.get("name"),
                    population=planet_data.get("population"),
                    terrains=planet_data.get("terrains"),
                    climates=planet_data.get("climates"),
                )
            except DatabaseError as e:
                logger.error(f"Error saving planet {planet_data.get('name')}: {e}")
                continue

        self.stdout.write(
            self.style.SUCCESS("Successfully filled the database with planet data")
        )
