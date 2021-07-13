from django.contrib import admin

from .models import Post, PostComment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'published', 'preview', 'author')
    empty_value_display = '-empty-'


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'published', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
