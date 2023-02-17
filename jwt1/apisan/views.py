from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from apisan.customauth import CustumAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustumAuthentication]
    Permission_classes = [IsAuthenticated]
   