from django.http import HttpResponse
from django.shortcuts import render
from Two.models import Student

# Create your views here.

def index(requests):
    return HttpResponse('Two index')

def add_student(requests):
    student = Student()
    student.s_name = 'Jenny'
    student.s_age = 27
    student.save()
    return HttpResponse('Add Succes : %s.'%student.s_name)

def get_students(requests):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    #return HttpResponse('Student List')
    return render(requests,"student_list.html")





