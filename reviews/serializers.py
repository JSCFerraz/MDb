from rest_framework import serializers
from users.serializers import UserReviewSerializer
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    critic = UserReviewSerializer(read_only=True)

    def create(self, validated_data: dict) -> Review:
        return Review.objects.create(**validated_data)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]

        read_only_fields = ["id", "critic", "movie"]
