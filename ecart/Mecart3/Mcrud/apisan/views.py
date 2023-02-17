from pstats import Stats
import statistics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Mcrud.settings import ProTest
from .models import stu
from .serializers import StudentSerializer
import datetime
from bson import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
# from ecart.settings import ProTest
from rest_framework.views import APIView
# Create your views here.



class testAPI(APIView):
    def post(self,request):
        try:
            Data=request.data
            # Data['createdOn']=datetime.now()
            # Data['createdBy']
            ProTest.student.insert_one(Data)
            print('-----------------')
            message={
                "message":"data added successfully"
            }
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={'enternal server error'}
            return JsonResponse({'error':'error','message':message,'status':500})
    
    def get(self,request):
        try:
            data=[]
            id = request.GET.get('id')
            if id:
                print('....')
                get_data= ProTest.student.find({'_id':ObjectId(id)})
                print('ok')
            else:  
                get_data=ProTest.student.find()
            for i in get_data:
                i['id']=str(i['_id'])
                del i['_id']
                data.append(i)
               
            return JsonResponse({'success':'success','status':200,'data':data})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500})
        
    def put(self,request):
        try:
            Data=request.data
            ProTest.student.update_one({"_id":ObjectId(Data['id'])},{"$set":Data})
            message="data update successfull"
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
        
        
    def delete(self,request):
        try:
            id=request.GET.get('id')
            ProTest.student.delete_one({'_id':ObjectId(id)})
            message="data delete successfull"
            return JsonResponse({'message':message,})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
        
########################################################
    #    if request.method == 'GET':
    #     tutorials = Tutorial.objects.all()
        
    #     title = request.GET.get('title', None)
    #     if title is not None:
    #         tutorials = tutorials.filter(title__icontains=title)
        
    #     tutorials_serializer = TutorialSerializer(tutorials, many=True)
    #     return JsonResponse(tutorials_serializer.data, safe=False)










#####################################################
   
class POSTAPI(APIView):
    def post(self,request):
        try:
            Data= request.data
            
            serializer=StudentSerializer(data=Data)
            if serializer.is_valid():
                serializer.save()
            message={
                "message":"data added successfully"
            }
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={'enternal server error'}
            return JsonResponse({'error':'error','message':message,'status':500})
        
        
        
    def get(self,request):
        try:
            # Data= Student.objects.all()
            # print(Data)
            Data= ProTest.stu.find()#{'_id':ObjectId(id)})
            # Data =  Student.objects.all()
            # l= request.GET.get( Data)
            for sl in Data:
                sl['id']=str([sl['_id']])
                del sl['_id']
                print('jjj',sl)
           
           
               
            return JsonResponse({'success':'success','status':200,'data':Data})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500})
            
            
            
        
    
    
    
   
   