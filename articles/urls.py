from django.urls import path
from articles import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name="article_list_view"),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name="article_detail_view"),
    path('<int:article_id>/comment/', views.CommentView.as_view(), name="comment_view"),
    path('<int:article_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name="like_view"),
]