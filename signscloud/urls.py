"""singscloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from supermarket.views import brands_list, brand_detail, stores_list, store_detail, deals_list, deal_detail, subscribe,usersSubscribed,test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', brands_list),
    path('stores/', stores_list),
    path('deals/', deals_list),
    path('store/<int:pk>/', store_detail),
    path('brand/<int:pk>/', brand_detail),
    path('deal/<int:pk>/', deal_detail),
    path('subscribe/', test),
    path('users-subscribed/<int:store_id>/', usersSubscribed),
    path('auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
