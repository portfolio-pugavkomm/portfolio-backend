from django.db.models import TextChoices


class TypeOfPublicationChoices(TextChoices):
    ARTICLE = "a", "Article"
    CONFERENCE = "c", "Conference"
