from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)