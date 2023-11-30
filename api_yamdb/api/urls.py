from django.urls import include, path
from rest_framework import routers

from api.views import CommentsViewSet


router = routers.SimpleRouter()
router.register(r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments/', CommentsViewSet,
                basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
