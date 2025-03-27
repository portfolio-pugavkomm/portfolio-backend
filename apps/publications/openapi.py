from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.publications.tags import PUBLICATION_TAG

list_publications_doc = extend_schema_view(
    get=extend_schema(tags=(PUBLICATION_TAG,), summary="Get list of publications")
)
