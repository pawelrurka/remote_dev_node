from django.contrib import admin
from django.utils.html import format_html
from .models import Idea, Vote


class VoteInLine(admin.TabularInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status','show_url']
    list_filter = ['status']
    inlines = [
        VoteInLine
    ]

    def show_url(self, obj):
        if (obj.idea_url) is None:
            return 'NO URL'
        else:
            return format_html(f'<a href="{obj.idea_url}" target="_blank">{obj.idea_url}</a>')

    show_url.short_description = "URL Idea"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']

