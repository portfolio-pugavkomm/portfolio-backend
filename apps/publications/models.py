from django.db import models

from apps.publications.defs import TypeOfPublicationChoices


class PublicationModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type_of_publication = models.CharField(choices=TypeOfPublicationChoices)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=2, default="en")
    publication_date = models.DateField()

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ("-publication_date",)

    def __str__(self) -> str:
        return f"{self.title}-{self.publisher}-{self.publication_date}"
