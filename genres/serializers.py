from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]
