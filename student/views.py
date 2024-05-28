from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Student,Course
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    return HttpResponse("This is student app homepage")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')

            if name and email:  # Check if both fields are provided
                student = Student(name=name, email=email)
                student.save()
                return JsonResponse({"message": "Student registered successfully!"})
            else:
                return JsonResponse({"error": "Missing name or email"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)

def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        if students.exists():
            students_list = list(students.values())
            return JsonResponse({"students": students_list})
        else:
            return JsonResponse({"students": "No students found!"})
        
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return JsonResponse({
        "id": student.id,
        "name": student.name,
        "email": student.email
    })
    
@csrf_exempt    
def course(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            courseCode=data.get('courseCode')
            courseName=data.get('courseName')
            if courseCode and courseName:
                course=Course(courseCode=courseCode,courseName=courseName)
                course.save()
                return JsonResponse({"message":"Course registered successfully!"})
            else:
                return JsonResponse({"error":"Missing course code or course name"},status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON data"},status=400)
    
    elif request.method=="GET":
    #show course
        courses=Course.objects.all()
        
        if(courses.exists()):
            courses_list=list(courses.values())
            return JsonResponse({"courses":courses_list})
        else:
        
            return JsonResponse({"message":"No courses found!"})