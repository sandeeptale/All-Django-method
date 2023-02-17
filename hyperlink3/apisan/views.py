# GenericAPIView and Model Mixin
from .models import Student
from django.shortcuts import render
from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from .models import Student

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  
   