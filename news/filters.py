from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post, Author

class PostFilter(FilterSet):
    date_post = DateTimeFilter(field_name='date_post', lookup_expr='gte')
    author = ModelChoiceFilter(queryset=Author.objects.all())
    class Meta:
        model = Post
        fields = {'heading':['icontains'],
                  'rating_post':['gt', 'lt'],
                  'date_post':['exact'],
                  'author':['exact', 'gte', 'lte']
                  }

