import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(blank=True, default=False)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    critic = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        blank=True,
        null=True,
    )
