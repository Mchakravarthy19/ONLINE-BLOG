from django.contrib import admin
from .models import JournalEntry
from .models import Feedback

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Fields to show in list view
    search_fields = ('title', 'content')           # Makes these fields searchable
    list_filter = ('created_at',)                  # Adds filter sidebar
    ordering = ('-created_at',)                    # Orders entries by newest first


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'short_message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('rating',)

    def short_message(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    short_message.short_description = 'Message'