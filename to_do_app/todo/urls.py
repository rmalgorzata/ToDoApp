from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.task_index, name="task_index"),
    path('<int:pk>/', views.task_detail, name="task_detail"),
    path('task/create/', views.create_task, name="create_task"),
    path('my_task/', views.TasksByUser.as_view(), name='my_task'),
    path('task_status_change/', views.change_task_status, name='change_status'),
    path('task_search/', views.search, name='search_task'),
]