# serializers.py

from rest_framework import serializers
from .models import CourseCreationModel,CourseProjectsModel,CourseOutlineModel,CourseOutlineVideoModel,CourseFieldRealtedContent

class CourseCreationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCreationModel
        fields = '__all__'

class CourseFieldRealtedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseFieldRealtedContent
        fields="__all__"

class CourseProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseProjectsModel
        fields="__all__"


class CourseOutlineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseOutlineModel
        fields="__all__"


class CourseOutlineVideosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseOutlineVideoModel
        fields="__all__"       