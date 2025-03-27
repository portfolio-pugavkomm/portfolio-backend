from typing import Any, Generator

from django.utils.timezone import now
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.education.models import EducationModel, EducationPlaceModel
from apps.education.serializers import EducationSerializer

fake = Faker()


def generator_education() -> Generator[EducationModel, None, Any]:
    while True:
        education_place, _ = EducationPlaceModel.objects.get_or_create(
            country_name=fake.country(), city=fake.city(), place_name=fake.text(60)
        )
        yield EducationModel.objects.create(
            title=fake.text(250),
            description=fake.text(500),
            start_year=fake.random_int(1996, now().year),
            end_year=fake.random_int(1996, now().year),
            place=education_place,
        )


class TestHttpGetListOfEducation(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("education-list")

    def test_get_education_list(self) -> None:
        education_generator = generator_education()
        education_list = [next(education_generator) for _ in range(3)]
        education_json_list = [EducationSerializer(ed).data for ed in education_list]
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(response.json(), education_json_list)
