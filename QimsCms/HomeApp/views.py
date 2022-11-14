from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')
    
def course1(request):
    return render (request, 'course-one.html')