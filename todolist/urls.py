from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task.html', views.add_task, name='add_task'),
    path('completed.html', views.completed, name='completed'),
    path('delete.html/<str:task_id>/', views.delete, name='delete'),
    path('remaining.html', views.remaining, name='remaining'),
    path('task_detail.html/<str:task_id>/', views.task_detail, name='task_detail'),
    path('toggle_complete.html/<str:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('remove_task.html/<str:task_id>/', views.remove_task, name='remove_task'),
]
 