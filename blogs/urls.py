from django.urls import path
from blogs.apps import BlogsConfig
from blogs import views

app_name = BlogsConfig.name

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    path('blogs/detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
