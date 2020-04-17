"""autotest_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from backend import views
from django.conf.urls import url


from rest_framework.routers import DefaultRouter
from backend.views2 import apiGroupViewSet, apiViewSet

router = DefaultRouter()
router.register(r'apiGroup2', apiGroupViewSet)
router.register(r'api2', apiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    path('getApiGroup/<int:projId>/', views.getApiGroup),
    path('updateApiGroup/<int:projId>/', views.updateApiGroup),
    path('getApi/<int:projId>/<int:apiGroupId>/', views.getApi),
    path('updateApi/', views.updateApi),
    path('addApi/', views.addApi),
    url(r'^', include(router.urls)),
]
