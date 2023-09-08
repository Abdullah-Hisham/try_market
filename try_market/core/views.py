from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets
from django.db.models import Q
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import *
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class product_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
@api_view(['GET'])

def seller_product(request,pk):
    if request.method == 'GET':
        s = seller.objects.all().filter(pk = pk)
        p = product.objects.all().filter(seller_name__id = str(s.values()[0]['id']))
        serializer = ProductSerializer(p,many = True)
        return Response(serializer.data)
#@api_view(['POST','GET'])
# def order_post(request,pk):
#     if request.method == 'GET':
#         serializer = OrderSerializer(order.objects.all() , many = True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         p = get_object_or_404(product,pk=pk)
#         order_create = order.objects.create(product_id = p)
#         serializer = OrderSerializer(order.objects.all(),many = True)
#         return Response(serializer.data)

class order_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

def tryy(request): 
    c = request.data
    p = type(c)
    response = {
        'k':str(p)
    }
    return JsonResponse(response)
class review_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = reviews.objects.all()
    serializer_class = ReviewsSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
@api_view(['GET'])
def product_reviews(request,pk):
    if request.method == "GET":
        p = product.objects.all().filter(pk = pk )
        r = reviews.objects.all().filter(product__id = str(p.values()[0]['id']))
        serializer = ReviewsSerializer(r , many = True)
        return Response(serializer.data)
@api_view(['GET'])
def product_info(request,pk):
    seller_n = product.objects.all().filter(pk =pk)
    serializer = Product_info_Serializers(seller_n,many = True)
    s_n = seller.objects.all().filter(pk = seller_n.values()[0]['seller_name_id'])
    serializer2 = SellerSerializer(s_n, many = True)
    return Response(serializer2.data)
class auth(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }

        return Response(content)
@api_view(['POST'])
def make_order(request,pk):
    order_n = order()
    order_n.name = request.data['name']
    order_n.quantity = request.data['quantity']
    order_n.adress = request.data['adress']
    order_n.phone_num = request.data['phone_num']
    p = product.objects.get(pk = pk )
    order_n.product_id = p
    pproduct = get_object_or_404(product, pk = pk)
    qquantity = int(request.POST.get('quantity'))
    p.quantity -= qquantity
    p.save()
    order_n.save()
    return Response(status=status.HTTP_201_CREATED)
def count_sell_product(request,pk):
    
    pass