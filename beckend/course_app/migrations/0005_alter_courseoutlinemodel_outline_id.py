# Generated by Django 5.1.1 on 2024-09-17 02:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_courseoutlinemodel_outline_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoutlinemodel',
            name='outline_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
