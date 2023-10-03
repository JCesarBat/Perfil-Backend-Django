from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
class order_processor(APIView):
        
        
        def post(self,request):
                mount=0
                try:
                            
                        orders=json.loads(request.body).get('orders')
                        criterion=json.loads(request.body).get('criterion')
                  
                except:
                        return  Response('the Json content is wrowng.......')
             
                
                if criterion not in  ['completed','canceled','pending']:
                        return Response('The criterion dont exisit......')
                for order in orders:
                        if order['price']<=0:
                                return Response(' the price of the object '+order['item']+" is incorrect....." )
                 
                
                for order in orders:
                        object_price=0
                        if order['status']==criterion:
                                object_price=order['quantity']*order["price"]                

                        mount+=object_price
                        
                return Response(mount)
# Create your views here.

