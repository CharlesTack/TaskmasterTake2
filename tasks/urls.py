from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
]
