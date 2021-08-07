from django import forms

from .models import Note, NoteComment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text_ru',)
        labels = {'text_ru': 'Russian text'}
        help_text = {'text_ru': 'Add russian text'}


class NoteCommentForm(forms.ModelForm):
    class Meta:
        model = NoteComment
        fields = ('text',)
        labels = {'text': 'Text'}
        help_text = {'text': 'Comment text'}
        widgets = {'text': forms.Textarea(attrs={'cols': '40', 'rows': '4'})}
