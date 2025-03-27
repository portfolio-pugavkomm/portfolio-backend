from rest_framework import serializers

from apps.education.models import EducationModel, EducationPlaceModel


class EducationPlaceSerializer(serializers.ModelSerializer[EducationPlaceModel]):
    class Meta:
        model = EducationPlaceModel
        fields = (
            "place_name",
            "country_name",
            "city",
        )


class EducationSerializer(serializers.ModelSerializer[EducationModel]):
    place = EducationPlaceSerializer()

    class Meta:
        model = EducationModel
        fields = (
            "id",
            "title",
            "description",
            "start_year",
            "end_year",
            "place",
        )
