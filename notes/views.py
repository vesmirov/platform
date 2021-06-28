from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
)

from .models import Note, Comment
from .forms import NoteForm, CommentForm
from .permissions import AdminPermission

User = get_user_model()


class IndexView(RedirectView):
    permanent = True
    url = reverse_lazy('notes')


class NoteListView(ListView):
    model = Note
    template_name = 'notes/notes.html'
    paginate_by = 6


class NoteCreateView(LoginRequiredMixin, AdminPermission, CreateView):
    model = Note
    template_name = 'notes/new.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(self.request.POST or None)
        return context


class NoteUpdateView(LoginRequiredMixin, AdminPermission, UpdateView):
    model = Note
    template_name = 'notes/new.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.note_id = self.kwargs['pk']
        form.instance.is_edited = True
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('note', kwargs={'pk': pk})
        return success_url


class NoteDeleteView(LoginRequiredMixin, AdminPermission, DeleteView):
    model = Note
    success_url = reverse_lazy('notes')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('note', kwargs={'pk': pk})
        return success_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.note_id = self.kwargs['pk']
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        dataset = get_object_or_404(Comment, pk=kwargs['comment_pk'])
        dataset.delete()
        return redirect('note', pk=kwargs['pk'])

    def get(self, request, **kwargs):
        return redirect('note', pk=kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['comment_pk'])
        if (self.request.user == comment.author 
                or self.request.user.is_superuser):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied()
