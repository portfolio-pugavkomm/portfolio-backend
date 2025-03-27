from rest_framework.generics import ListAPIView

from apps.education.models import EducationModel
from apps.education.openapi import list_education_doc
from apps.education.serializers import EducationSerializer


@list_education_doc
class ListEducationApiView(ListAPIView[EducationModel]):
    queryset = EducationModel.objects.all()
    pagination_class = None
    serializer_class = EducationSerializer
