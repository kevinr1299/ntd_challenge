from http import HTTPStatus
from random import randint

from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase

from planets.models import Planet


class PlanetAPITests(APITestCase):
    def setUp(self):
        self.faker = Faker()

    def _create_planet(self):
        self.planet = Planet.objects.create(
            name=self.faker.name(),
            population=self.faker.random_int(min=1000, max=1000000),
            climates=self.faker.random_int(min=1, max=5),
            terrains=self.faker.random_int(min=1, max=5),
        )

    def test_create_planet(self):
        data = {
            "name": self.faker.name(),
            "population": self.faker.random_int(min=1000, max=1000000),
            "climates": self.faker.random_int(min=1, max=5),
            "terrains": self.faker.random_int(min=1, max=5),
        }
        response = self.client.post(
            reverse("api:planets:api-planets-list"),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_create_planet_repeated_name(self):
        self._create_planet()
        data = {
            "name": self.planet.name,
            "population": self.faker.random_int(min=1000, max=1000000),
            "climates": self.faker.random_int(min=1, max=5),
            "terrains": self.faker.random_int(min=1, max=5),
        }
        response = self.client.post(
            reverse("api:planets:api-planets-list"),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_list_planets(self):
        self._create_planet()
        response = self.client.get(reverse("api:planets:api-planets-list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertGreaterEqual(len(response.data), 0)

    def test_list_planets_invalid_page(self):
        response = self.client.get(
            reverse("api:planets:api-planets-list"), {"page": randint(2, 1000)}
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_retrieve_planet(self):
        self._create_planet()
        response = self.client.get(
            reverse(
                "api:planets:api-planets-detail",
                kwargs={"pk": self.planet.pk},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_retrieve_nonexistent_planet(self):
        response = self.client.get(
            reverse(
                "api:planets:api-planets-detail",
                kwargs={"pk": 9999},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_update_planet(self):
        self._create_planet()
        data = {
            "name": self.planet.name,
            "population": self.faker.random_int(min=1000, max=1000000),
            "climates": self.faker.random_int(min=1, max=5),
            "terrains": self.faker.random_int(min=1, max=5),
        }
        response = self.client.patch(
            reverse(
                "api:planets:api-planets-detail",
                kwargs={"pk": self.planet.pk},
            ),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_delete_planet(self):
        self._create_planet()
        response = self.client.delete(
            reverse(
                "api:planets:api-planets-detail",
                kwargs={"pk": self.planet.pk},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
