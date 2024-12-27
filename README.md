from django.utils import timezone
from datetime import timedelta
from news.models import Author, Post, Category, Comment
from django.contrib.auth.models import User

user1 = User.objects.create_user('user1', password='password1')
user2 = User.objects.create_user('user2', password='password2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

category1 = Category.objects.create(name='Технологии')
category2 = Category.objects.create(name='Наука')
category3 = Category.objects.create(name='Спорт')
category4 = Category.objects.create(name='Культура')

article1 = Post.objects.create(
    title='Новая технология в программировании',
    text='Обзор новых трендов в программировании...',
    author=author1,
    post_type='article',
    created_at=timezone.now()
)
article1.categories.add(category1, category2)  # Присвоение двух категорий

article2 = Post.objects.create(
    title='Спортивные достижения 2023 года',
    text='Обзор самых выдающихся спортивных событий...',
    author=author2,
    post_type='article',
    created_at=timezone.now() - timedelta(days=1)  # Установка даты добавления
)
article2.categories.add(category3)

news1 = Post.objects.create(
    title='Научное открытие 2023 года',
    text='Изучение нового аспекта квантовой физики...',
    author=author1,
    post_type='news',
    created_at=timezone.now() - timedelta(days=2)
)
news1.categories.add(category1, category2)

comment1 = Comment.objects.create(
    post=article1,
    user=user1,
    text='Интересная статья!',
    created_at=timezone.now()
)
comment2 = Comment.objects.create(
    post=article1,
    user=user2,
    text='Согласен с мнением автора.',
    created_at=timezone.now() - timedelta(hours=1)
)
comment3 = Comment.objects.create(
    post=article2,
    user=user1,
    text='Супер, благодарю за информацию!',
    created_at=timezone.now()
)
comment4 = Comment.objects.create(
    post=news1,
    user=user2,
    text='Научные исследования действительно впечатляют.',
    created_at=timezone.now() - timedelta(hours=2)
)

article1.like()
article1.like()
article1.dislike()  # Один dislike

article2.like()

news1.like()

comment1.like()
comment2.dislike()
comment3.like()
comment4.like()

author1.update_rating_author()
author2.update_rating_author()

best_author = Author.objects.order_by('-rating_author').first()
print(f'Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating_author}')

best_article = Post.objects.order_by('-rating_post').first()
print(f'Дата добавления: {best_article.created_at}, Автор: {best_article.author.user.username}, '
      f'Рейтинг: {best_article.rating_post}, Заголовок: {best_article.title}, Превью: {best_article.text[:50]}')

comments_to_best_article = Comment.objects.filter(post=best_article)
for comment in comments_to_best_article:
    print(f'Дата: {comment.created_at}, Пользователь: {comment.user.username}, '
          f'Рейтинг: {comment.rating_comment}, Текст: {comment.text}')
