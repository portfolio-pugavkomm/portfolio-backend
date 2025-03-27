from rest_framework import serializers

from apps.publications.models import PublicationModel


class PublicationSerializer(serializers.ModelSerializer[PublicationModel]):
    class Meta:
        model = PublicationModel
        fields = (
            "id",
            "title",
            "description",
            "type_of_publication",
            "publisher",
            "language",
            "publication_date",
        )
