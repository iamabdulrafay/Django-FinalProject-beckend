from rest_framework import viewsets
from .models import UserMessage, AdminReply
from .serializers import UserMessageSerializer, AdminReplySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class UserMessageViewSets(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AdminReplyViewSets(viewsets.ModelViewSet):
    queryset = AdminReply.objects.all()
    serializer_class = AdminReplySerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        message_id = self.request.data.get('message')
        user_message = get_object_or_404(UserMessage, pk=message_id)
        serializer.save(admin=self.request.user, message=user_message)
