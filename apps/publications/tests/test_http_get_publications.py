import random
from typing import Any, Generator

from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.publications.models import PublicationModel
from apps.publications.serializers import PublicationSerializer

fake = Faker()


def create_publication() -> Generator[PublicationModel, None, Any]:
    while True:
        yield PublicationModel.objects.create(
            title=fake.text(100),
            publisher=fake.city(),
            publication_date=fake.date(),
            description=fake.text(300),
            language="en",
            type_of_publication=random.choice(["a", "c"]),
        )


class TestGetListOfPublications(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("publications-list")

    def test_get_one_publication(self) -> None:
        publication = next(create_publication())
        publication_json = PublicationSerializer(publication).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_publications = response.json()
        self.assertEqual(len(response_publications), 1)

        self.assertEqual(response_publications[0], publication_json)

    def test_get_few_publications(self) -> None:
        publication_generator = create_publication()
        publications = [next(publication_generator) for _ in range(3)]
        publications_json = [PublicationSerializer(publication).data for publication in publications]

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_publications = response.json()
        self.assertEqual(len(response_publications), 3)
        self.assertCountEqual(response_publications, publications_json)
