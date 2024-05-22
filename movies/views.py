from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from FlixApi.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
	queryset = Movie.objects.all()
	serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
	queryset = Movie.objects.all()
	serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
	permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
	queryset = Movie.objects.all()

	def get(self, request):
		return response.Response(
			data={'message': 'Movie stats'},
			status=status.HTTP_200_OK
		)
