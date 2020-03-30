# from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from . import models

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    # sort by date
    queryset = models.Article.objects.order_by('-date')
    template_name = 'articles/article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comments'] = self.object.comments.all().order_by('-date')

        return ctx

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body',]
    # set login url to point to our custom login route
    login_url = 'login'

    # sets article creation author to current user 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'articles/article_edit.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.edited = timezone.now()
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ['text']
    login_url = 'login'
    template_name = 'comments/comment_new.html'

    def form_valid(self, form):
        # get article pk from url parameter:
        # https://stackoverflow.com/questions/15754122/url-parameters-and-logic-in-django-class-based-views-templateview
        article_pk = self.kwargs.get('pk')
        article = models.Article.objects.get(pk=article_pk)

        # bind user and article to comment form
        form.instance.author = self.request.user
        form.instance.article = article
        
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Comment
    template_name = 'comments/comment_delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('article_detail', args=[str(self.kwargs.get('article_pk'))])

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Comment
    fields = ['text']
    login_url = 'login'
    template_name = 'comments/comment_edit.html'

    def form_valid(self, form):
        form.instance.edited = timezone.now()
        return super().form_valid(form)

def article_vote(request, *args, **kwargs):
    article = models.Article.objects.get(pk=kwargs['pk'])
    vote = models.ArticleVote.objects.filter(voter=request.user, article=article)
    if vote:
        vote.delete()
    else:
        vote = models.ArticleVote(voter=request.user, article=article)
        vote.save()

    return HttpResponseRedirect(reverse_lazy('article_list'))