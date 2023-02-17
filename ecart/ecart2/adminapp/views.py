from audioop import error
import datetime
from unittest import result
from bson import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
from ecart2.settings import ProTest
from rest_framework.views import APIView
# Create your views here.



class empAPI(APIView):
    def post(self,request):
        try:
            Data=request.data
            # Data['createdOn']=datetime.now()
            # Data['createdBy']
            ProTest.employee.insert_one(Data)
            print('-----------------')
            message={
                "message":"data added successfully"
            }
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={'enternal server error'}
            return JsonResponse({'error':'error','message':message,'status':500})
    
    # def get(self,request):
    #     try:
    #         data=[]
    #         k =[]
    #         id = request.GET.get('id')
    #         if id:
    #             print('....')
    #             get_data= ProTest.employee.find({'_id':ObjectId(id)})
    #             print('ok')
    #             message={
    #             "message":"one data got successfully"
    #         }
    #         else:  
    #             get_data=ProTest.employee.find()
    #         for i in get_data:
    #             i['id']=str(i['_id'])
    #             del i['_id']
    #             data.append(i)
            
               
    #         return JsonResponse({'success':'success','status':200,'data':data})
    #     except Exception as e:
    #         message={"message":"enternal server error',{}".format(e)}
    #         return JsonResponse({'error':'error','message':message,'status':500})
   
    def get(self,request):
        try:
            data=[]
            k=[]
            id = request.GET.get('id')
            
        
        
        
    
            if id:
               
                s1= ProTest.employee.find({'_id':ObjectId(id)})
            
            else:  
                
                s1=ProTest.employee.find()
                
                print(s1)
            print('jjjjjjjjjjjjjjjjjjjjjjjjjj')    
            for i in s1:
                
                if i["Salary"]=="200000":
                        k.append(i)
                        print('yyy',k)
            
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
            ProTest.employee.update_one({"_id":ObjectId(Data['id'])},{"$set":Data})
            message="data update successfull"
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
        
        
    def delete(self,request):
        try:
            id=request.GET.get('id')
            ProTest.employee.delete_one({'_id':ObjectId(id)})
            message="data delete successfull"
            return JsonResponse({'message':message,})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500}) 
        
    ############################################################################################################################    
        
        
        
class newapi(APIView):
     def get(self,request):
        try:
            data=[]
            k =[]
            id = request.GET.get('id')
            if id:
                print('....')
                get_data= ProTest.test.find({'_id':ObjectId(id)})
                print('ok')
                message={
                "message":"one data got successfully"
            }
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
   
    
     def put(self,request):
        try:
            #    s1= ProTest.test.update_many({" {_id:637b6655e574152b2cf62bcd}"},{"$push":{"red":"red"}}) 
            # s1= ProTest.test.update_many({"colordetail"},{"$push":{"#f00":"skyred"}}) 
            Data=request.data
            # ProTest.test.update_one({"_id":ObjectId(Data['id'])},{"$set":Data})
            # message={"data update successfull"}
            # ProTest.test.update_one({}, {"$set": {"colordetail" : {'color': 'red', 'value': "#f00"}}},function(error, result){
            #   if(error){
            #     console.log('error');
            #     } else {
            #     console.log('success');
            #     }
            #     });

            ProTest.test.update_one({"_id": ObjectId(Data['id']) ,"colordetail": {"$elemMatch": {'value': 'sandeep',}}}, { "$set": {"colordetail.$.color": "vishal"}})
            message={"data update successfull"}
            
            return JsonResponse({'success':'success','message':message})
        except Exception as e:
            message={"message":"enternal server error',{}".format(e)}
            return JsonResponse({'error':'error','message':message,'status':500})
        
        
        
           # s1= ProTest.test.find({'_id':ObjectId(id)})
                #    s1= ProTest.test.update_many({" {_id:637b6655e574152b2cf62bcd}"},{"$push":{"red":"red"}}) 
                # s1= ProTest.test.update_many({"colordetail"},{"$push":{"#f00":"skyred"}}) 
                # print(s1)
                
                #    "goodsType": "SWEETS",
                #     "capacityValue": "5",
                #     "freightCharges": "5",
                #     "packagingQty": "5",
                #     "packagingMode": "ROLL"
                # },
                #  for item in val:
                #     #     print('kkkkk',item)
                        
                #     if val["cars"]=="Fiat":
                #         print('kkkk',val)
                                                    
                                        # k.append(n)
                                        
#=====================================================================================

class allApi(APIView):
     def get(self,request):
        try:
            data=[]
            k =[]
            j =[]
            
            get_data=ProTest.post.find()
            for i in get_data:
                i['id']=str(i['_id'])
                del i['_id']
                data.append(i)
                print(data,"llll")
                for s in i["goods"]:
                    print(s,"hhhhhh")
                    # if  s["packagingMode"]=="BORI":
                    
                # for t in s["goodsType"]:
                #     print(t,"oooo")
                        
                    for n in s['packagingMode']:
                        j.append(n)
                        print(''.join(n),"mccm")
                        # if n["packagingMode"]=="BORI":
                        #     print(n,"mmmm")
                        #     k.append(n)
                            
                        
                    
                
                return JsonResponse({'success':'success','status':200,'data':j})
        except Exception as e:
                message={"message":"enternal server error',{}".format(e)}
                return JsonResponse({'error':'error','message':message,'status':500})
                