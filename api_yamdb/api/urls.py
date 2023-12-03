from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentsViewSet, ReviewsViewSet
from users.views import SignUpView, TokenView, UserViewSet


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
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', TokenView.as_view(), name='token_obtain'),
]
