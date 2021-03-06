from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', views.AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update-post'),
    path('article/delete/<int:pk>/', views.DeletePostView.as_view(), name='delete-post'),
    path('category/<int:cat>/', views.CategoryView, name='category'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('like/<int:pk>', views.LikeView, name='like-post'),
    path('article/<int:pk>/add_comment/', views.AddCommentView.as_view(), name='add-comment'),
]