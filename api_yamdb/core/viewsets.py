from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from api.paginators import Pagination
from api.permissions import IsAdminOrReadOnly


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
