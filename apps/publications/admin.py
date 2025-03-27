from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.publications import models


@admin.register(models.PublicationModel)
class PublicationModelAdmin(ModelAdmin):  # type: ignore
    list_display = ("id", "title", "publication_date")
    compressed_fields = True
