from django.shortcuts import render, redirect
from todo.models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.template.defaultfilters import yesno
from django.http import HttpResponseRedirect
from django.urls import reverse



def task_index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_index.html', context)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }
    return render(request, 'task_detail.html', context)    


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('task_detail', pk=post.pk)
    else:
        form = TaskForm()        
    return render(request, 'create_task.html', {'form':form})


class TasksByUser(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'my_task.html'
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


def change_task_status(request):
    tasks = Task.objects.all()
    task_id = request.GET['task_id']
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return HttpResponseRedirect(reverse('task_detail', args=[task.id]))


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            tasks = Task.objects.filter(name__icontains=q)
            return render(request, 'task_search_results.html', {'tasks': tasks, 'query': q})
    return render(request, 'task_search.html', {'error': error})