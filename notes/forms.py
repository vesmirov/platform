from django import forms

from .models import Note, Comment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text_ru', 'text_en')
        labels = {
            'text_ru': 'Russian text',
            'text_en': 'English text',
        }
        help_text = {
            'text_ru': 'Add russian text',
            'text_en': 'Add english text',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Text'}
        help_text = {'text': 'Comment text'}
        widgets = {'text': forms.Textarea(attrs={'cols': '40', 'rows': '4'})}