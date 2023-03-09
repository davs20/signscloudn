from django.shortcuts import render
from supermarket.models import Brands, Stores, Deals, User
from supermarket.serializer import BrandSerializer, StoreSerializer, DealSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework import generics, permissions, serializers
from oauth2_provider.decorators import protected_resource
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from signscloud.celery import debug_task


@protected_resource()
def brands_list(request):
    if request.method == 'GET':
        brands = Brands.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@protected_resource()
def brand_detail(request, pk):
    try:
        brand = Brands.objects.get(pk=pk)
    except Brands.DoesNotExist:
       return HttpResponse(status=404)
    
    
    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(brand, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        brand.delete()
        return HttpResponse(status=204)

@protected_resource()
def stores_list(request):
    if request.method == 'GET':
        stores = Stores.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@protected_resource()
def store_detail(request, pk):
    try:
        store = Stores.objects.get(pk=pk)
    except Stores.DoesNotExist:
       return HttpResponse(status=404)
    
    
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DealSerializer(store, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        store.delete()
        return HttpResponse(status=204)

@protected_resource()
def deals_list(request):
    if request.method == 'GET':
        deals = Deals.objects.all()
        serializer = DealSerializer(deals, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DealSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@protected_resource()
def deal_detail(request,pk):
    try:
        deal = Deals.objects.get(pk=pk)
    except Deals.DoesNotExist:
       return HttpResponse(status=404)
    
    
    if request.method == 'GET':
        serializer = DealSerializer(deal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DealSerializer(deal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        deal.delete()
        return HttpResponse(status=204)
    
    
@protected_resource()
def subscribe(request):
    data = JSONParser().parse(request)
    user = User.objects.get(pk=data['user_id'])
    store = Stores.objects.get(pk=data['store_id'])
    user.stores.add(store)
    return JsonResponse(StoreSerializer(store).data, status=201)

def test(request):
    
    return JsonResponse({"response": "ok"})

@protected_resource()
def usersSubscribed(request,  store_id):
    store =  Stores.objects.get(pk=store_id)
    serializers =  UserSerializer(store.users, many=True)
    return JsonResponse(serializers.data, status=201, safe=False) 
    
    
    
    