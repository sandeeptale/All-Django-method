# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[OrderingFilter]
    search_fields=[SearchFilter]
    # search_fields=['city']
    search_fields=['^name']