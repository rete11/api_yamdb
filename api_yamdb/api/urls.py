from django.urls import include, path
from rest_framework import routers

from api.views import ReviewsViewSet


router = routers.SimpleRouter()
router.register(r'titles/(?P<title_id>[^/.]+)/reviews/', ReviewsViewSet,
                basename='reviews')


urlpatterns = [
    path('v1/', include(router.urls)),
]
