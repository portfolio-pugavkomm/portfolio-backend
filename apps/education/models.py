from django.db import models


class EducationPlaceModel(models.Model):
    country_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    place_name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Education Place"
        verbose_name_plural = "Education Places"
        ordering = ("country_name", "city", "place_name")

    def __str__(self) -> str:
        return f"{self.place_name}::{self.city}::{self.country_name}"


class EducationModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    start_year = models.PositiveBigIntegerField()
    end_year = models.PositiveBigIntegerField()
    place = models.ForeignKey(EducationPlaceModel, related_name="educations", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
        ordering = ["-start_year", "-end_year"]

    def __str__(self) -> str:
        return f"{self.title}::{self.start_year}::{self.end_year}"
