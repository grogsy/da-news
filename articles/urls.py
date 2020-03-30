from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/vote/', views.article_vote, name='article_vote'),
    # here, pk has to be associated with the main model for this view(in this case its comment)
    # article is a secondary model in this context, so it has to have a different name,
    # otherwise django will throw an error if you give article in as pk in the url instead of comment
    path('<int:article_pk>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:article_pk>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit')
]