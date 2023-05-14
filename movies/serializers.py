from rest_framework import serializers
from genres.serializers import GenreSerializer
from movies.models import Movie
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:

        movie_genres = validated_data.pop("genres")

        movie_obj = Movie.objects.create(**validated_data)

        for genre in movie_genres:

            genre_obj = Genre.objects.filter(name__iexact=genre["name"]).first()

            if not genre_obj:
                genre_obj = Genre.objects.create(**genre)

            movie_obj.genres.add(genre_obj)

        return movie_obj

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

        read_only_fields = ["id", "user"]
