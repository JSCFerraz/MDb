from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.permissions import IsAdminOrReadOnly


class MovieView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)
