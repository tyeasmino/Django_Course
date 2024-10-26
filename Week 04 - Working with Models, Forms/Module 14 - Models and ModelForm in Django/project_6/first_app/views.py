from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    student = models.Student.objects.all() 


    return render(request, 'first_app/index.html', {'data' : student}) 



def delete_student(request, roll): 
    deleteStudent = models.Student.objects.get(pk = roll).delete()
    return redirect('home') 