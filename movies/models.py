import uuid
from django.db import models


class Movie(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField()
    premiere = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies", blank=True
    )
    genres = models.ManyToManyField(
        "genres.Genre",
        related_name="movies",
    )
