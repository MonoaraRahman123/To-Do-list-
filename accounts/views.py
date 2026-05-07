from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from students.models import Student
from tasks.models import Task

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_admin():
        total_students = Student.objects.count()
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(is_completed=True).count()
        context = {
            'total_students': total_students,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': total_tasks - completed_tasks,
        }
        return render(request, 'accounts/admin_dashboard.html', context)
    else:
        student = getattr(request.user, 'student_profile', None)
        tasks = Task.objects.filter(user=request.user)
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(is_completed=True).count()
        context = {
            'student': student,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': total_tasks - completed_tasks,
            'recent_tasks': tasks[:5]
        }
        return render(request, 'accounts/student_dashboard.html', context)
