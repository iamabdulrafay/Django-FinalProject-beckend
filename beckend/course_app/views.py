# views.py

from rest_framework import viewsets
from .models import CourseCreationModel,CourseProjectsModel,CourseOutlineModel,CourseOutlineVideoModel,CourseFieldRealtedContent
from .serializers import CourseCreationModelSerializer,CourseProjectsModelSerializer,CourseOutlineModelSerializer,CourseOutlineVideosModelSerializer,CourseFieldRealtedContentSerializer
from rest_framework.permissions import AllowAny
class CourseCreationModelViewSet(viewsets.ModelViewSet):
    queryset = CourseCreationModel.objects.all()
    serializer_class = CourseCreationModelSerializer
    permission_classes = [AllowAny] 

class CourseFieldRealtedContentViewSet(viewsets.ModelViewSet):
    queryset=CourseFieldRealtedContent.objects.all()
    serializer_class=CourseFieldRealtedContentSerializer   
    permission_classes = [AllowAny]  

class CourseProjectsModelViewSet(viewsets.ModelViewSet):
    queryset = CourseProjectsModel.objects.all()
    serializer_class =CourseProjectsModelSerializer
    permission_classes = [AllowAny] 
class CourseOutlineModelViewSet(viewsets.ModelViewSet):
    queryset = CourseOutlineModel.objects.all()
    serializer_class = CourseOutlineModelSerializer
    permission_classes = [AllowAny] 
class CourseOutlineVideoViewSet(viewsets.ModelViewSet):
    queryset=CourseOutlineVideoModel.objects.all()
    serializer_class=CourseOutlineVideosModelSerializer
    permission_classes = [AllowAny] 