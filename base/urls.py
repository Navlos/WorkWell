from django.urls import path
from . import views

from .views import TaskList,TaskDetails,CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home, name = 'home'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('register',views.register, name = 'register'),
    path('tasks',TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/',TaskDetails.as_view(), name = 'task'),
]
