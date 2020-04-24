from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Post








class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-posted']
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
   

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content','image']
    success_url = reverse_lazy('home')
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Post
    template_name = 'post_form.html'
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'about.html', {'title': 'About'})







