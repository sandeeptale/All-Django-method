from django.contrib import admin
from .models import stud

# class adminpanel(admin.ModelAdmin):
# admin.site.register(Student)

@admin.register(stud)
class admindata(admin.ModelAdmin):
   list_display=  ['stupid','stuname','stupas','Comment']