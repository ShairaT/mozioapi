"""MozioPolygons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from mozioApp.views import index, ProviderDetail, ProviderAll, ProviderList, ServiceAreaAll, ServiceAreaDetail, ServiceAreaList, query
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('provider/add', ProviderList.as_view()),
    path('provider', ProviderAll.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),
    path('serviceArea/add', ServiceAreaList.as_view()),
    path('serviceArea', ServiceAreaAll.as_view()),
    path('serviceArea/<int:pk>/', ServiceAreaDetail.as_view()),
    path('query/', query),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
