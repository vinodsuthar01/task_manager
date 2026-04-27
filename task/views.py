from django.shortcuts import render, redirect
from task.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user = request.user)

        pending_task = tasks.filter(status = 'Pending').count()
        completed_task = tasks.filter(status = 'Completed').count()

        today = date.today()
        next_5_days = today+timedelta(days=5)

        due_soon_tasks = tasks.filter(due_date__range=[today,next_5_days],status='Pending')
        
        return render(request,'home.html',{'pending_task':pending_task,'completed_task':completed_task,'due_soon_tasks':due_soon_tasks})
    else:
        return render(request,'home.html')
    
@login_required
def tasks_list(request):
    tasks = Task.objects.filter(user = request.user)

    q = request.GET.get('q')
    status = request.GET.get('status')
    if q:
        tasks = tasks.filter(title__icontains = q)
    
    if status:
        tasks = tasks.filter(status=status)

          

    return render(request,'dashboard.html',{'tasks':tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        discription = request.POST.get('discription')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        if Task.objects.filter(title=title).exists():
            messages.error(request,'title already exists')
            return redirect('add_task')

        task = Task.objects.create(
            user=request.user,
            title = title,
            discription = discription,
            status = status,
            priority = priority,
            due_date = due_date
        )
        task.save()
        messages.success(request,'Task added succussfully...')
        return redirect('dashboard')

    return render(request, 'add_task.html')

@login_required
def edit_task(request,id):
    task = Task.objects.get(pk = id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.discription = request.POST.get('discription')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.due_date  = request.POST.get('due_date')

        task.save()
        messages.success(request,'updated successfully ...')
        return redirect('dashboard')

    return render(request,'add_task.html',{'task':task})

@login_required
def delete_task(request,id):
    task = Task.objects.get(pk = id)
    if task is not None:
        task.delete()
        messages.success(request,'task deleted successfully...')
        return redirect('dashboard')
    else:
        messages.error(request,'task doesn''t exits')
        return redirect('dashboard')
    

@login_required
def change_status(request,id):
    task = Task.objects.get(pk = id)

    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
        messages.success(request,'status changed...')
        return redirect('dashboard')
        
    return render(request,'change_status.html',{'task':task})


@login_required
def mark_done(request,id):
    task = Task.objects.get(id = id)
    task.status = 'Completed'
    task.save()
    return redirect('home')
    