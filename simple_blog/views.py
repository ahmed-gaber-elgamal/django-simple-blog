from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, cat):
    category = get_object_or_404(Category, id=cat)
    category_post = Post.objects.filter(category=cat)
    context = {'category_post': category_post, 'category': category}
    return render(request, 'category.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'