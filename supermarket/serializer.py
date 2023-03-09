from django.urls import path, include
from django.contrib.auth.models import Group
from django.contrib import admin
from supermarket.models import Brands, Deals, Stores, User
admin.autodiscover()
from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brands
        fields = ['id', 'name', 'logo']

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ['id', 'name', 'store', 'image', 'price']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ['id', 'brand', 'identifier', 'name', 'address']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']