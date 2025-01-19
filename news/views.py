from django.views.generic import ListView
from .models import *

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


