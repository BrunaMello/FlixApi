from rest_framework import serializers

from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
	rate = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Movie
		fields = '__all__'

	def get_rate(self, obj):
		return 5

	def validate_release_date(self, value):
		if value.year < 1900:
			raise serializers.ValidationError('Release date must be after 1900')
		return value

	def validate_resume(self, value):
		if len(value) > 200:
			raise serializers.ValidationError('Comment must be below 200 characters long')
		return value
