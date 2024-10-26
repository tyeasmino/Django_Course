from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    student = models.Student.objects.all() 


    return render(request, 'first_app/index.html', {'data' : student}) 