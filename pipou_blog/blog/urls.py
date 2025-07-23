from django.urls import path
from .views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDelete

urlpatterns = [
    path('', BlogHome.as_view(), name="index"),
    path('blog/create/', BlogPostCreate.as_view(), name="create"),
    path('blog/edit/<int:pk>', BlogPostEdit.as_view(), name="edit"),
    path('blog/delete/<int:pk>', BlogPostDelete.as_view(), name="delete")
]
