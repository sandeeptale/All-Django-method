from django.db import models




class stud(models.Model):
    stupid =models.IntegerField()
    stuname=models.CharField(max_length=70)
    stupas=models.CharField(max_length=70)
    Comment=models.CharField(max_length=40, default='not available')
    class Meta:
        db_table ='stu'
       
    
