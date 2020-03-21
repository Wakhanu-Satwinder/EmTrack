# api/urls.py
from django.urls import path
from rest_framework import generics,viewsets,routers
from . import views
from .views import EmployeeAPIView,EmployeeViewSet
router = routers.SimpleRouter()
router.register(r'employees',views.EmployeeViewSet)

urlpatterns = [
    path('', EmployeeAPIView.as_view()),
    # path('detaiil/', EmployeAPIView.as_view()),
    path(r'^employees/$',views.EmployeeViewSet)
    ]

urlpatterns=router.urls
