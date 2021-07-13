from django.contrib import admin

from .models import Note, NoteComment


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'published', 'author')
    empty_value_display = '-empty-'


class NoteCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'note', 'published', 'author')


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteComment, NoteCommentAdmin)
