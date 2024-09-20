# views.py

from rest_framework import viewsets
from .models import CourseCreationModel,CourseProjectsModel,CourseOutlineModel,CourseOutlineVideoModel,CourseFieldRealtedContent
from .serializers import CourseCreationModelSerializer,CourseProjectsModelSerializer,CourseOutlineModelSerializer,CourseOutlineVideosModelSerializer,CourseFieldRealtedContentSerializer

class CourseCreationModelViewSet(viewsets.ModelViewSet):
    queryset = CourseCreationModel.objects.all()
    serializer_class = CourseCreationModelSerializer

class CourseFieldRealtedContentViewSet(viewsets.ModelViewSet):
    queryset=CourseFieldRealtedContent.objects.all()
    serializer_class=CourseFieldRealtedContentSerializer    
class CourseProjectsModelViewSet(viewsets.ModelViewSet):
    queryset = CourseProjectsModel.objects.all()
    serializer_class =CourseProjectsModelSerializer
class CourseOutlineModelViewSet(viewsets.ModelViewSet):
    queryset = CourseOutlineModel.objects.all()
    serializer_class = CourseOutlineModelSerializer
class CourseOutlineVideoViewSet(viewsets.ModelViewSet):
    queryset=CourseOutlineVideoModel.objects.all()
    serializer_class=CourseOutlineVideosModelSerializer