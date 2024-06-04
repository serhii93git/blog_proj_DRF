from django.urls import path, include
from rest_framework import routers
from post.views import PostViewSet
from creator.views import CreatorView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'creator', CreatorView, basename='creator')

urlpatterns = [
        path('', include(router.urls)),
]
