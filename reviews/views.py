from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from reviews.models import Review
from movies.models import Movie
from reviews.serializers import ReviewSerializer
from reviews.permissions import IsAllowedUserOrReadOnly


class ReviewView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAllowedUserOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"

    def perform_create(self, serializer) -> None:
        movie_data = get_object_or_404(Movie, id=self.kwargs.get(self.lookup_url_kwarg))
        serializer.save(critic=self.request.user, movie=movie_data)
