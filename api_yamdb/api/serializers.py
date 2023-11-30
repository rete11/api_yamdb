from django.db.models import Avg
from rest_framework import serializers

from titles.models import Reviews, Title


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = ('rating',)

    def get_rating(self, obj):
        average = (
            Reviews.objects
            .filter(title=obj)
            .aggregate(Avg('score'))['score__avg']
        )

        return average
