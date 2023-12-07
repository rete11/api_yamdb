from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.paginators import Pagination
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from titles.models import Title


class CategoryGenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class BaseReviewsAndCommentsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = Pagination

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            raise MethodNotAllowed('PUT')
        return super().update(request, *args, **kwargs)
