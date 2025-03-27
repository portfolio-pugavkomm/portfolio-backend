from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.education.tags import EDUCATION_TAG

list_education_doc = extend_schema_view(
    get=extend_schema(
        summary="Get education history",
        tags=(EDUCATION_TAG,),
    )
)
