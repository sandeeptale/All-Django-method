# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django.shortcuts import render



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    