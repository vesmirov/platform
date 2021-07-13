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

from .forms import PostForm, PostCommentForm
from .models import Post, PostComment
from .permissions import AdminPermission

User = get_user_model()


class IndexView(RedirectView):
    """Main page, which redirects to posts page"""

    permanent = True
    url = reverse_lazy('posts:posts')


class PostListView(ListView):
    """Latest posts"""

    model = Post
    template_name = 'posts/posts.html'
    paginate_by = 6


class PostCreateView(LoginRequiredMixin, AdminPermission, CreateView):
    """Create a new post"""

    model = Post
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    """
        Detail post with comments
    """

    model = Post
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = PostCommentForm(self.request.POST or None)
        return context


class PostUpdateView(LoginRequiredMixin, AdminPermission, UpdateView):
    """
        Edit post
    """

    model = Post
    template_name = 'posts/new.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        form.instance.is_edited = True
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('posts:post', kwargs={'pk': pk})
        return success_url


class PostDeleteView(LoginRequiredMixin, AdminPermission, DeleteView):
    """
        Delete post
    """

    model = Post
    success_url = reverse_lazy('posts:posts')


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    """
        Add a comment to post
    """

    model = PostComment
    form_class = PostCommentForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('posts:post', kwargs={'pk': pk})
        return success_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class PostCommentDeleteView(LoginRequiredMixin, View):
    """
        Delete comment
    """

    def post(self, request, *args, **kwargs):
        dataset = get_object_or_404(PostComment, pk=kwargs['comment_pk'])
        dataset.delete()
        return redirect('posts:post', pk=kwargs['pk'])

    def get(self, request, **kwargs):
        return redirect('posts:post', pk=kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(PostComment, pk=kwargs['comment_pk'])
        if (self.request.user == comment.author
                or self.request.user.is_superuser):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied()
