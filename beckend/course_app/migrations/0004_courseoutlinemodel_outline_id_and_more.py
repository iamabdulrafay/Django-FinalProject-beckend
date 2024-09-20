# Generated by Django 5.1.1 on 2024-09-17 02:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_courseprojectsmodel_delete_coursedetailsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoutlinemodel',
            name='outline_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='courseprojectsmodel',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='course_app.coursecreationmodel'),
        ),
        migrations.CreateModel(
            name='CourseOutlineVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200)),
                ('course_video', models.FileField(blank=True, null=True, upload_to='course_videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlines_videos', to='course_app.courseoutlinemodel')),
            ],
        ),
    ]
