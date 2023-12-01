from rest_framework import serializers

from titles.models import Review


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
