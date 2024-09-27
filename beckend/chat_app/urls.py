from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserMessageViewSets,AdminReplyViewSets

router = DefaultRouter()
router.register(r'user-messages', UserMessageViewSets)
router.register(r'admin-replies', AdminReplyViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
