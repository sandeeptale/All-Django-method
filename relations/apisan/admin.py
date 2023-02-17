from django.contrib import admin
from .models import Singer, Song

# class adminpanel(admin.ModelAdmin):
# admin.site.register(Student)

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
   list_display=  ['id','name','gender']
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   list_display =['id','title','singer','duration']
   