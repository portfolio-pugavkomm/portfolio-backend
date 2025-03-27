from rest_framework.generics import ListAPIView

from apps.publications.models import PublicationModel
from apps.publications.openapi import list_publications_doc
from apps.publications.serializers import PublicationSerializer


@list_publications_doc
class ListPublicationApiView(ListAPIView[PublicationModel]):
    queryset = PublicationModel.objects.all()
    serializer_class = PublicationSerializer
    filterset_fields = ["title", "publication_date"]
