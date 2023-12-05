from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.filters import TitleFilter
from api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    GetTitleSerializer,
    PostTitleSerializer,
    ReviewSerializer,
)
from categories.models import Category
from genres.models import Genre
from reviews.models import Review
from titles.models import Title


class Pagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ReviewsViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = Pagination

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )

        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        )

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            raise MethodNotAllowed(self.request.method)
        return super().get_serializer_class()


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = Pagination

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=title
        )

        return review.comments.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=title
        )
        serializer.save(
            author=self.request.user,
            review=review
        )

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            raise MethodNotAllowed(self.request.method)
        return super().get_serializer_class()


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    lookup_field = 'slug'


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    lookup_field = 'slug'


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = GetTitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TitleFilter
    ordering_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            raise MethodNotAllowed(self.request.method)
        if self.action == 'retrieve' or self.action == 'list':
            return GetTitleSerializer
        return PostTitleSerializer
