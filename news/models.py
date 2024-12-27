from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    rating_author = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating_author(self):
        if self.rating_author > 1:
            rating_post_sum = sum(post.rating_post * 3 for post in self.post.all())
            rating_comment_sum = sum(comment.rating_comment for comment in self.comment.all())
            total_rating_author = rating_comment_sum+rating_post_sum
            return total_rating_author
        return self.rating_author
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    type_post = models.BooleanField(default=True)
    date_post = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255)
    content = models.TextField()
    rating_post = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', through='PostCategory')

    def like(self):
        self.rating_post+=1
        self.save()

    def dislike(self):
        if self.rating_post > 1:
            self.rating_post-=1
            self.save()

    def preview(self):
        text = self.content
        if len(text) > 124:
            return text[0:124] + '...'
        else:
            return text

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text_comment = models.CharField(max_length=255)
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment+=1
        self.save()

    def dislike(self):
        if self.rating_comment > 1:
            self.rating_comment-=1
            self.save()


