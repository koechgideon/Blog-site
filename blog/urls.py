from django.urls import path
from blog import views
from .views import PostListView
 

urlpatterns = [
    path('files/upload/', views.upload_files, name='upload_files'),
    path('', PostListView.as_view(), name='Blog-Home'),
    path('about/', views.about, name='Blog-About')
] 