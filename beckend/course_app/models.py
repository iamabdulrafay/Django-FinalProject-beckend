# models.py

from django.db import models
import math
from django.db import models
import uuid
import random
class CourseCreationModel(models.Model):
    course_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    course_heading = models.CharField(max_length=100, unique=True)
    course_tags = models.CharField(max_length=60, blank=True, null=True)
    course_thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    course_description = models.TextField(max_length=500, blank=True)
    course_instructor = models.CharField(max_length=50)
    course_price = models.IntegerField()

    def __str__(self):
        return self.course_heading


class CourseFieldRealtedContent(models.Model):
    course=models.ForeignKey(CourseCreationModel,on_delete=models.CASCADE,related_name="course_field_related_content")
    course_short_title=models.CharField(max_length=50)
    course_level=models.CharField(max_length=50)
    course_related_image=models.ImageField(upload_to="course_related_photo",blank=True,null=False)
    


class CourseProjectsModel(models.Model):
    course = models.ForeignKey(CourseCreationModel, on_delete=models.CASCADE, related_name='projects')
    course_project_num = models.CharField(max_length=100, blank=False, null=False)
    course_related_images = models.ImageField(upload_to='course_project_intro/', blank=True, null=True)

    def __str__(self):
        return f"Details for {self.course.course_heading}"

class CourseOutlineModel(models.Model):
    course = models.ForeignKey(CourseCreationModel, on_delete=models.CASCADE, related_name='outlines',default=1)
    outline_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    outline_heading = models.CharField(max_length=100, blank=False, null=False)
    outline_desc = models.TextField(default="Enter outline here")
    
    def __str__(self):
        return f"Outline: {self.outline_heading} for {self.course.course_heading}"


class CourseOutlineVideoModel(models.Model):
      course_outline = models.ForeignKey(CourseOutlineModel, on_delete=models.CASCADE, related_name='outline_videos',default=1)
      video_name=models.CharField(max_length=200)
      course_video=models.FileField(upload_to='course_videos/', blank=True, null=True)
      course_video_description=models.TextField(default="wrte your vidoe description here")
      def __str__(self) -> str:
          return f'{self.video_name}'
