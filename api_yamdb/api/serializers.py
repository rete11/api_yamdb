from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from titles.models import Comment, Review, Title
from categories.models import Category
from genres.models import Genre
from titles.validators import validate_years


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)
        lookup_field = 'slug'


class GetTitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('__all__',)

    def get_rating(self, obj):
        average = (
            Review.objects
            .filter(title=obj)
            .aggregate(Avg('score'))['score__avg']
        )

        return average


class PostTitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    genre = SlugRelatedField(
        slug_field='slug', queryset=Genre.objects.all(), many=True
    )
    year = serializers.IntegerField()
    description = serializers.CharField(required=False)

    def to_representation(self, value):
        return GetTitleSerializer(self.instance).data

    def validate_year(self, value):
        return validate_years(value)

    class Meta:
        model = Title
        fields = '__all__'
