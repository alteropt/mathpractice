from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.tasks_home, name='tasks_home'),
	path('create', views.TaskCreateView.as_view(), name='create'),
	path('<int:type_id>/', views.task_type, name='type'),
	path('<int:type_id>/<int:pk>/', views.TasksDetailView.as_view(), name='task-detail'),
	path('<str:type_id>/<int:pk>/update', views.TasksUpdateView.as_view(), name='task-update'),
	path('<str:type_id>/<int:pk>/delete', views.TasksDeleteView.as_view(), name='task-delete'),
]
