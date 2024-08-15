from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog-list'),
    path('product/<int:id>/', BlogDetailView.as_view(), name='blog-detail')
]
