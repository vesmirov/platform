from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Note(models.Model):
    """Users notes"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    published = models.DateTimeField('date published', auto_now_add=True)
    edited = models.DateTimeField('date edited', auto_now=True)
    is_edited = models.BooleanField('has post been edited', default=False)
    text_ru = models.TextField('russian text')
    text_en = models.TextField('english text', blank=True, null=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        if self.title:
            return self.title
        return self.text[:12]


class Comment(models.Model):
    """Comments for notes"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    published = models.DateTimeField("date published", auto_now_add=True)
    text = models.TextField('text')
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.text[:12]
