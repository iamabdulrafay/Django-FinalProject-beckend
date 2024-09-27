from django.contrib import admin
from .models import UserMessage, AdminReply

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_stamp', 'message')  # Fields to display in the list view
    search_fields = ('user__username', 'message')    # Enable search by username and message
    list_filter = ('time_stamp',)                     # Filter by timestamp

class AdminReplyAdmin(admin.ModelAdmin):
    list_display = ('admin', 'reply_message', 'time_stamp', 'message')  # Fields to display
    search_fields = ('admin__username', 'message')                      # Enable search
    list_filter = ('time_stamp',)                                       # Filter by timestamp

# Register the models with the admin site
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(AdminReply, AdminReplyAdmin)
