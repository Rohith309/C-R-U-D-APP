from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student

def home_page(request):
    students = Student.objects.all()
    return render(request, "index.html", {'students': students})

def student_form(request):
    return render(request, 'Stud_form.html')

def save_student(request):
    if request.method == 'POST':
        idno = request.POST.get('id')
        stdname = request.POST.get('name')
        course = request.POST.get('course')
        fee = request.POST.get('fee')

        if not idno or not stdname or not course or not fee:
            messages.error(request, "All fields are required.")
            return redirect('student_form')

        if not Student.objects.filter(id=idno).exists():
            student = Student(id=idno, name=stdname, course=course, fee=fee)
            student.save()
            messages.success(request, "Student details saved successfully.")
        else:
            messages.error(request, "Student details already exist.")

        return redirect('home_page')

    return redirect('student_form')

def read_stud(request):
    students = Student.objects.all()
    return render(request, 'Read_stud.html', {'students': students})

def delete(request):
    return render(request, "delete_stud.html")

def delete_student_form(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        deleted_count, _ = Student.objects.filter(id=id).delete()

        if deleted_count > 0:
            messages.success(request, "Student deleted successfully.")
        else:
            messages.error(request, "Student does not exist.")
        return redirect('home_page')
    return render(request, "delete_stud.html")

def search_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        return render(request, 'update_student.html', {'student': student})
    return render(request, 'update_student.html')

def update_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.fee = request.POST.get('fee')
        student.save()
        
        messages.success(request, 'Student details updated successfully!')
        return redirect('read_stud')
    return render(request, 'update_student.html')

