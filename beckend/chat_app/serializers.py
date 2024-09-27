from rest_framework import serializers
from .models import UserMessage,AdminReply
from django.contrib.auth.models import User


class AdminReplySerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminReply
        fields="__all__"        

class UserMessageSerializer(serializers.ModelSerializer):
    replies = AdminReplySerializer(many=True, read_only=True, source='adminreply_set')  # Use reverse relationship
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())


    class Meta:
        model = UserMessage
        fields = ['id', 'user', 'time_stamp', 'message', 'replies']  # Include replies


