from django.urls import path
from .views import Home,HomeView,PostDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView

urlpatterns=[
    path('',Home,name='home'),
    path('posts',HomeView.as_view(),name='allposts'),
    path('posts/<int:pk>',PostDetailView.as_view(),name='post-detail'), # pk - primary key
    path('posts/addpost',AddPostView.as_view(),name='add-post'),
    path('posts/updatepost/<int:pk>',UpdatePostView.as_view(),name='edit-post'),
    path('posts/deletepost/<int:pk>',DeletePostView.as_view(),name='delete-post'),
    path('posts/addcategory',AddCategoryView.as_view(),name='add-category'),
    path('category/<str:cat>/',CategoryView,name='category'),
    path('category-list',CategoryListView,name="category-list"),
    path('like/<int:pk>',LikeView,name="like-post"),
    path('posts/<int:pk>/comment/',AddCommentView.as_view(),name='comment'),
]