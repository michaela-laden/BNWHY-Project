from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bnwhy.api.models import Post, Comment, Category
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html',{})


class AlteryxListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=1).order_by('-date_posted')

class SQLListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=2).order_by('-date_posted')

class ShareListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=3).order_by('-date_posted')

class PythonListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=4).order_by('-date_posted')


class OCRListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=5).order_by('-date_posted')

class BlueListView(ListView):
    model = Post
    template_name = 'Alteryx.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category_id=6).order_by('-date_posted')


class UserPostListView(ListView):
    model = Post
    template_name = 'user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name ='posts-detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name ='posts_form.html'
    fields = ['title', 'category','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name ='comment_form.html'
    fields = ['text']

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        form.instance.post_id = post_id
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('posts-detail', kwargs={'pk':self.object.post_id})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name ='posts_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name ='post_confirm_delete.html'
    success_url = '/alteryx'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



