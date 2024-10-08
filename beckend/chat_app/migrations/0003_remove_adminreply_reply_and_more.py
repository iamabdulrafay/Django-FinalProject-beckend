# Generated by Django 5.1.1 on 2024-09-23 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_alter_adminreply_user_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminreply',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='adminreply',
            name='user_message',
        ),
        migrations.AddField(
            model_name='adminreply',
            name='message',
            field=models.TextField(default='write reply here'),
        ),
        migrations.AddField(
            model_name='adminreply',
            name='reply_message',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat_app.usermessage'),
        ),
    ]
