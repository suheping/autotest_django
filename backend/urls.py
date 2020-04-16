from django.urls import path
from backend import views1

urlpatterns = [
    path('apiGroup/', views1.ApiGroupList.as_view()),
    path('apiGroup/<int:pk>/', views1.ApiGroupDetail.as_view())
]
