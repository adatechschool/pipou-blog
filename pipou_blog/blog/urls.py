from django.urls import path
from .views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDelete

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('edit/<int:pk>', BlogPostEdit.as_view(), name="edit"),
    path('delete/<int:pk>', BlogPostDelete.as_view(), name="delete")
]
