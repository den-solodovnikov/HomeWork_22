from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "blogs/blog.html"
    context_object_name = "blogs"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ('title', 'content', 'image', 'is_published', 'views_counter')
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('blogs:blog_detail', kwargs={'pk': self.object.pk})


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ('title', 'content', 'image', 'is_published', 'views_counter')
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('blogs:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog')
    login_url = reverse_lazy('users:login')
