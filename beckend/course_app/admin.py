from django.contrib import admin
from .models import CourseCreationModel, CourseProjectsModel, CourseOutlineModel, CourseOutlineVideoModel,CourseFieldRealtedContent

class CourseProjectsInline(admin.StackedInline):
    model = CourseProjectsModel
    can_delete = True
    verbose_name_plural = 'Course Projects'
    extra = 1
    max_num = 5

class CourseOutlineInline(admin.TabularInline):
    model = CourseOutlineModel
    can_delete = True
    verbose_name_plural = 'Course Outlines'
    extra = 1
    max_num = 10

class CourseOutlineVideoInline(admin.TabularInline):
    model = CourseOutlineVideoModel
    verbose_name_plural = 'Course Videos'
    extra = 1
    max_num = 10

@admin.register(CourseCreationModel)
class CourseCreationModelAdmin(admin.ModelAdmin):
    inlines = [CourseProjectsInline, CourseOutlineInline]
    list_display = ('course_heading', 'course_instructor', 'course_price')
    search_fields = ('course_heading', 'course_instructor')

@admin.register(CourseProjectsModel)
class CourseProjectsAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_project_num')
    search_fields = ('course__course_heading', 'course_project_num')

@admin.register(CourseOutlineModel)
class CourseOutlineAdmin(admin.ModelAdmin):
    inlines = [CourseOutlineVideoInline]
    list_display = ('course', 'outline_heading')
    search_fields = ('course__course_heading', 'outline_heading')

@admin.register(CourseOutlineVideoModel)
class CourseOutlineVideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'course_outline')
    search_fields = ('video_name', 'course_outline__outline_heading')

@admin.register(CourseFieldRealtedContent)
class CourseFieldRealtedContentAdmin(admin.ModelAdmin):
    list_display = ('course_short_title', 'course_level',"course_related_image")
    # search_fields = ('video_name', 'course_outline__outline_heading')
