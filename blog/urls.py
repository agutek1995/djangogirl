from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('jacek_post_list/', views.post_list, name='post_list'),
]