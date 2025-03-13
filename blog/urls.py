from django.urls import path
# technically can just say import views but this shows that views belongs to the same folder
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list")
]
