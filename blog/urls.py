from django.urls import path
from .views import PostListView


urlpatterns = [
    path('', PostListView.as_view(template_name='home.html'), name='home')
]