from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.education.models import EducationModel, EducationPlaceModel


@admin.register(EducationModel)
class EducationModelAdmin(ModelAdmin):  # type: ignore
    list_display = ("id", "title", "start_year", "end_year", "place")


@admin.register(EducationPlaceModel)
class EducationPlaceModelAdmin(ModelAdmin):  # type: ignore
    list_display = ("id", "place_name", "country_name", "city")
