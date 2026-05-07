from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def student_list(request):
    if not request.user.is_admin():
        return redirect('dashboard')
    
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | 
            Q(student_id__icontains=query) | 
            Q(department__icontains=query)
        )
    else:
        students = Student.objects.all()
    
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {'page_obj': page_obj})

@login_required
def student_add(request):
    if not request.user.is_admin():
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})

@login_required
def student_edit(request, pk):
    if not request.user.is_admin():
        return redirect('dashboard')
    
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student'})

@login_required
def student_delete(request, pk):
    if not request.user.is_admin():
        return redirect('dashboard')
    
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

@login_required
def student_profile(request):
    student = getattr(request.user, 'student_profile', None)
    return render(request, 'students/student_profile.html', {'student': student})
