from django.contrib import admin
from . import models
from . import forms

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    # form = forms.CustomArticleForm
    inlines = [
        CommentInline,
    ]

    model = models.Article

class CommentAdmin(admin.ModelAdmin):
    model = models.Comment
    form = forms.CustomCommentForm
    add_form = forms.CustomCommentForm

# Register your models here.
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)