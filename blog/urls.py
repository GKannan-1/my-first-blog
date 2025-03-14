from django.urls import path
# technically can just say import views but this shows that views belongs to the same folder
from . import views
from typing_extensions import Any

urlpatterns: list[Any] = [
    path("", views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail,
         name='post_detail'),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
]
