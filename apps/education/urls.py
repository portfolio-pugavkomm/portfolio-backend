from django.urls import path

from apps.education import views

urlpatterns = [
    path("", views.ListEducationApiView.as_view(), name="education-list"),
]
