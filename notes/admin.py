from django.contrib import admin

from .models import Note, Comment


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'published', 'author')
    empty_value_display = '-empty-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'note', 'published', 'author')


admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)
