from rest_framework import serializers
from django.db.models import Avg

from titles.models import Comment, Review, Reviews, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        fields = "__all__"
        model = Review
        read_only_fields = ("title",)

    def validate(self, attrs):
        author = attrs["author"]
        title = attrs["title"]
        if Review.objects.filter(author=author, title=title).exists():
            raise serializers.ValidationError(
                f"Вы уже оставляли отзыв на {title}"
            )

        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('review',)


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
