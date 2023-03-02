from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'base/index.html')



class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    

def register(request):
    return render(request, 'auth/register.html')



class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = "base/task_list.html"
    context_object_name = 'tasks'
    
class TaskDetails(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "base/task_detail.html"
    context_object_name = 'task'


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')