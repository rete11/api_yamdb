from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import ModelViewSet

from api.filters import TitleFilter
from api.paginators import Pagination
from api.permissions import IsAdminOrReadOnly
from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    GetTitleSerializer,
    PostTitleSerializer,
    ReviewSerializer,
)
from categories.models import Category
from core.viewsets import BaseReviewsAndCommentsViewSet, CategoryGenreViewSet
from genres.models import Genre
from reviews.models import Review
from titles.models import Title


class ReviewsViewSet(BaseReviewsAndCommentsViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = self.get_title()

        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentsViewSet(BaseReviewsAndCommentsViewSet):
    serializer_class = CommentSerializer

    def get_review(self, title):
        return get_object_or_404(
            Review, pk=self.kwargs.get('review_id'), title=title
        )

    def get_queryset(self):
        title = self.get_title()
        review = self.get_review(title)

        return review.comments.all()

    def perform_create(self, serializer):
        title = self.get_title()
        review = self.get_review(title)
        serializer.save(author=self.request.user, review=review)


class CategoryViewSet(CategoryGenreViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).select_related('category').prefetch_related('genre')
    serializer_class = GetTitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TitleFilter
    ordering_fields = ('name',)

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            raise MethodNotAllowed('PUT')
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return GetTitleSerializer
        return PostTitleSerializer
