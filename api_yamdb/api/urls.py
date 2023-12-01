from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentsViewSet, ReviewsViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/',
    ReviewsViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments/',
    CommentsViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/auth/signup/', , name='signup'),
    # path('v1/auth/token/', , name='token_obtain'),
]
