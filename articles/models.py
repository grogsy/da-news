from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    edited = models.DateTimeField(null=True, blank=True)

    @property
    def synopsis(self):
        body = self.body[:255].strip()
        return '{}...'.format(body)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name='comments' # allows us to access 1-m relationship as: article.comments --> gives us all comments
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.article.id)])

class ArticleVote(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='votes'
    )