from django.urls import path
from . import views

urlpatterns = [
    # Task URLs
    path('', views.task_list, name='task_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<str:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<str:task_id>/update/', views.task_update, name='task_update'),
    path('tasks/<str:task_id>/delete/', views.task_delete, name='task_delete'),
    
    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<str:user_id>/update/', views.user_update, name='user_update'),
    path('users/<str:user_id>/delete/', views.user_delete, name='user_delete'),
]