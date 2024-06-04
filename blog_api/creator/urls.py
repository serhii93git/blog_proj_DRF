from django.urls import path, include
from rest_framework import routers
from .views import CreatorView

router = routers.DefaultRouter()
router.register(r'creator', CreatorView)

urlpatterns = [
        path('', include(router.urls)),
]
