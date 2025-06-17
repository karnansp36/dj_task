from typing import Any, Dict, Union
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from datetime import datetime

from .models import Task, User
from .forms import TaskForm, UserForm

# Task CRUD Views
def task_list(request: HttpRequest) -> HttpResponse:
    """
    View to display all tasks
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request: HttpRequest, task_id: str) -> HttpResponse:
    """
    View to display details of a specific task
    """
    try:
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/task_detail.html', {'task': task})
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect('task_list')

def task_create(request: HttpRequest) -> HttpResponse:
    """
    View to create a new task
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Get form data
            data = form.cleaned_data
            
            # Create task object
            task = Task(
                title=data['title'],
                description=data['description'],
                status=data['status'],
                priority=data['priority'],
                due_date=data['due_date'],
                completed=data['completed'],
                tags=data['tags'],
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            # Save task to MongoDB
            task.save()
            
            messages.success(request, "Task created successfully!")
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'action': 'Create'
    })

def task_update(request: HttpRequest, task_id: str) -> HttpResponse:
    """
    View to update an existing task
    """
    try:
        task = Task.objects.get(id=task_id)
        
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                # Get form data
                data = form.cleaned_data
                
                # Update task fields
                task.title = data['title']
                task.description = data['description']
                task.status = data['status']
                task.priority = data['priority']
                task.due_date = data['due_date']
                task.completed = data['completed']
                task.tags = data['tags']
                task.updated_at = datetime.now()
                
                # Save changes to MongoDB
                task.save()
                
                messages.success(request, "Task updated successfully!")
                return redirect('task_detail', task_id=task.id)
        else:
            # Pre-populate form with task data
            initial_data = {
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'priority': task.priority,
                'due_date': task.due_date,
                'completed': task.completed,
                'tags': ', '.join(task.tags) if task.tags else ''
            }
            form = TaskForm(initial=initial_data)
        
        return render(request, 'tasks/task_form.html', {
            'form': form,
            'task': task,
            'action': 'Update'
        })
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect('task_list')

def task_delete(request: HttpRequest, task_id: str) -> HttpResponse:
    """
    View to delete a task
    """
    try:
        task = Task.objects.get(id=task_id)
        
        if request.method == 'POST':
            # Delete the task from MongoDB
            task.delete()
            messages.success(request, "Task deleted successfully!")
            return redirect('task_list')
        
        return render(request, 'tasks/task_confirm_delete.html', {'task': task})
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect('task_list')

# User CRUD Views
def user_list(request: HttpRequest) -> HttpResponse:
    """
    View to display all users
    """
    users = User.objects.all()
    return render(request, 'tasks/user_list.html', {'users': users})

def user_create(request: HttpRequest) -> HttpResponse:
    """
    View to create a new user
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Get form data
            data = form.cleaned_data
            
            # Create user object
            user = User(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                created_at=datetime.now()
            )
            
            # Save user to MongoDB
            try:
                user.save()
                messages.success(request, "User created successfully!")
                return redirect('user_list')
            except Exception as e:
                messages.error(request, f"Error creating user: {str(e)}")
    else:
        form = UserForm()
    
    return render(request, 'tasks/user_form.html', {
        'form': form,
        'action': 'Create'
    })

def user_update(request: HttpRequest, user_id: str) -> HttpResponse:
    """
    View to update an existing user
    """
    try:
        user = User.objects.get(id=user_id)
        
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                # Get form data
                data = form.cleaned_data
                
                # Update user fields
                user.username = data['username']
                user.email = data['email']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                
                # Save changes to MongoDB
                try:
                    user.save()
                    messages.success(request, "User updated successfully!")
                    return redirect('user_list')
                except Exception as e:
                    messages.error(request, f"Error updating user: {str(e)}")
        else:
            # Pre-populate form with user data
            initial_data = {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            form = UserForm(initial=initial_data)
        
        return render(request, 'tasks/user_form.html', {
            'form': form,
            'user': user,
            'action': 'Update'
        })
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_list')

def user_delete(request: HttpRequest, user_id: str) -> HttpResponse:
    """
    View to delete a user
    """
    try:
        user = User.objects.get(id=user_id)
        
        if request.method == 'POST':
            # Delete the user from MongoDB
            user.delete()
            messages.success(request, "User deleted successfully!")
            return redirect('user_list')
        
        return render(request, 'tasks/user_confirm_delete.html', {'user': user})
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_list')