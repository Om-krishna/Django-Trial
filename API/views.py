from django.shortcuts import render
from django.http import HttpResponse
from .models import greetings
from rest_framework import viewsets
from .serializers import greetingsSerializer

def hii(request):
    return render(request, 'hii')
def hello(request):
    return render(request, 'hello')


# Create your views here.
class greetingsViewSet(viewsets.ModelViewSet):
    queryset = greetings.objects.all()
    serializer_class = greetingsSerializer
    
