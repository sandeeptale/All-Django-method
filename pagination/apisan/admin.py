from django.contrib import admin
from .models import Student

# class adminpanel(admin.ModelAdmin):
# admin.site.register(Student)

@admin.register(Student)
class admindata(admin.ModelAdmin):
   list_display=  ['id','name','city',]