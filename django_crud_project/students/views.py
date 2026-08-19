from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from .models import Student


def student_list(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")

        Student.objects.create(
            name=name,
            email=email,
            course=course
        )

    students = Student.objects.all()

    return render(
        request,
        "student_list.html",
        {
            "students": students
        }
    )
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.save()
        return redirect("student_list")

    return render(
        request,
        "edit_student.html",
        {
            "student": student
        }
    )
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("student_list") 