from django.urls import path

from apps.publications import views

urlpatterns = [
    path("", views.ListPublicationApiView.as_view(), name="publications-list"),
]
