from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='home'),  # Add this line for the root URL
    path('tasks/', views.task_list_view, name='task_list'), # You can keep this if you want /tasks/ to also work
    path('tasks/create/', views.create_task_view, name='create_task'),
]