import datetime
from bson import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
from ecart.settings import ProTest
from rest_framework.views import APIView
# Create your views here.



class testAPI(APIView):
    def post(self,request):
        try:
            Data=request.data
            # Data['createdOn']=datetime.now()
            # Data['createdBy']
            ProTest.test.insert_one(Data)
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
                get_data= ProTest.test.find({'_id':ObjectId(id)})
                print('ok')
            else:  
                get_data=ProTest.test.find()
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
            ProTest.test.update_one({"_id":ObjectId(Data['id'])},{"$set":Data})
            message="data update successfull"
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
        
        
    def delete(self,request):
        try:
            id=request.GET.get('id')
            ProTest.test.delete_one({'_id':ObjectId(id)})
            message="data delete successfull"
            return JsonResponse({'message':message,})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
                     