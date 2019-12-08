from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# to check if user is login if not redirected to login page in classbase view
from .models import Post
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def like_post(request, post_id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect('/')


def home(requests, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'posts': post,
        'is_liked': is_liked
    }

    return render(request, 'blog/home.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_post.html"
    context_object_name = 'posts'

    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')  # listing post in last added order


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # take that instance and set the author to current login user
        return super().form_valid(form)  # run form valid method in parent class(validate the form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', ]

    def form_valid(self, form):
        form.instance.author = self.request.user  # take that instance and set the author to current login user
        return super().form_valid(form)  # run form valid method in parent class(validate the form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
