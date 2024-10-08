from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

def serve_react(request):
    return render(request, 'build/index.html')

def index(request):
    return render(request, 'frontend/index.html')

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()