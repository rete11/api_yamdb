from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsOwnerOrReadOnly
from api.serializers import ReviewSerializer
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
