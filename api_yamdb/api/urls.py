from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import (
    CommentsViewSet,
    ReviewsViewSet,
    CategoryViewSet,
    TitleViewSet,
    GenreViewSet,
)


app_name = 'api'

router = routers.SimpleRouter()
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    CommentsViewSet,
    basename='comments'
)
router.register(
    'categories',
    CategoryViewSet,
    basename='сategories',
)
router.register(
    'titles',
    TitleViewSet,
    basename='titles',
)
router.register(
    'genres',
    GenreViewSet,
    basename='genres',
)

urlpatterns = [
    # path('v1/auth/signup/', , name='signup'),
    # path('v1/auth/token/', name='token_obtain'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/', include(router.urls)),
]
