from django.urls import path

from Blog import views

urlpatterns = [
    path('index/', views.Index.as_view(), name='post_list_url'),
    path('post/create/', views.PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),
    path('tags/', views.tag_list, name='tags_list_url'),
    path('tag/create', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),
]
