from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='signUp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('task-list/', views.GetTaskList.as_view(), name='tasklist'),
    path('task-add/', views.PostTask.as_view(), name='addtask'),
    path('task-update/', views.UpdateTask.as_view(), name='updatetask'),
    path('task-delete/', views.DeleteTask.as_view(), name='deletetask'),
    path('task-detail/', views.TaskDetail.as_view(), name='detail'),
    path('task-search/', views.SearchTask.as_view(), name= 'tasksearch'),
    path('task-filter-name/', views.FilterNmaeTask.as_view(), name='taskfiltername'),
    path('task-filter-createdAt/', views.FilterCreatedAt.as_view(), name= 'taskfiltercreatedat'),
]