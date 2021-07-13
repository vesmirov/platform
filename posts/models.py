from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """
        Users posts
    """

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    published = models.DateTimeField('date published', auto_now_add=True)
    title = models.CharField('post title', max_length=120)
    text = models.TextField('post text')

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        if self.title:
            return self.title
        return self.text[:12]


class PostComment(models.Model):
    """
        Comments for post
    """

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_comments'
    )
    published = models.DateTimeField("date published", auto_now_add=True)
    text = models.TextField('text')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.text[:12]
