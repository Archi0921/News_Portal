from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView )
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['time_now'] = datetime.utcnow()
        #context['next_sale'] = None
        #return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model =Post
    template_name = 'post.html'
    context_object_name = 'post'

#def CreatePost(request):
#    form = PostForm()
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/posts/')
#
#    return render(request, 'post_edit.html', {'form': form})

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


