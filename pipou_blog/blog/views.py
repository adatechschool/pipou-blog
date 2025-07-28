from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from django import forms

class BlogHome(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"

class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlogPostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index")

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class BlogPostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("index")

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
