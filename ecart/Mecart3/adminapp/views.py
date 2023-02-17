from audioop import error
import datetime
from unittest import result
from bson import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
import requests
from Mecart3.settings import ProTest
from rest_framework.views import APIView

# Create your views here.

class listAPI(APIView):
    def post(self,request):
        try:
            Data= request.data
            ProTest.student.insert_one(Data)
            message={"message":"data added successfully"}
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
                get_data= ProTest.login.find({'_id':ObjectId(id)})
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
    
    
    # def get(self,request):
    #     try:
    #         data=[]
    #         k=[]
    #         id = request.GET.get('id')
            
    #         if id:
               
    #             s1= ProTest.student.find({'_id':ObjectId(id)})
            
    #         else:  
                 
    #             s1=ProTest.student.find()
               
    #         print('eeeee',s1)
    #         print('jjjjjjjjjjjjjjjjjjjjjjjjjj')    
    #         for i in s1:
    #             print('shhhhs',i)
                
    #             for val in i["cars"]:
    #                 print('tttt',val)
    #                 if val["brand"]=='BMW':
    #                  for n in val :
    #                      if n = 

                
                    
                    
                #     # for item in val:
                #     #     print('kkkkk',item)
                        
                #     if val["cars"]=="Fiat":
                #         print('kkkk',val)
                                                    
                                        # k.append(n)
                                        
                                        # print('yyy',k)
    
                # val['id']=str(val['_id'])
                # del val['_id']
                # data.append(val)
        
        #     return JsonResponse({'success':'success','status':200,'data':k})
        # except Exception as e:
        #     message={"message":"enternal server error',{}".format(e)}
        #     return JsonResponse({'error':'error','message':message,'status':500})
    
    
    
    
    
    
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
        
        
class logAPI(APIView):
    def post(self,request):
        try:
        
            Data= request.data
            print(Data)
            get_data =   ProTest.login.find({"email":Data["email"]})
            print('kkkk',get_data)
            for i in  get_data:
                if i['email']==Data['email']:
                    
            # if get_data.count()>0:
                    print('oooo')
                    message={"message":"data already exist"}
                    return JsonResponse({'success':'success','message':message})
                
                else:
                    ProTest.login.insert_one(Data)
                    
                    message={"message":"data added successfully"}
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
                get_data= ProTest.login.find({'_id':ObjectId(id)})
                print('ok')
            else:  
                get_data=ProTest.login.find()
            for i in get_data:
                i['id']=str(i['_id'])
                del i['_id']
                data.append(i)
               
            return JsonResponse({'success':'success','status':200,'data':data})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500})
    