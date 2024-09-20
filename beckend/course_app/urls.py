from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseCreationModelViewSet, CourseProjectsModelViewSet,CourseOutlineVideoViewSet,CourseOutlineModelViewSet,CourseFieldRealtedContentViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'courses', CourseCreationModelViewSet)
router.register(r'course-related-content', CourseFieldRealtedContentViewSet)
router.register(r'course-project', CourseProjectsModelViewSet)
router.register(r'course-outlines', CourseOutlineModelViewSet)
router.register(r'course-outlines-videos', CourseOutlineVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]




# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
