from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'payables', views.PayableViewSet, basename='payables')
router.register(r'transactions', views.TransactionViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
    #path('payables/', views.PayableListView.as_view(), name='payables-status'),
    #path('payables/<str:payment_status>', views.PayableListView.as_view(), name='payables-status'),
    #path('payables/pending/<str:service_type>', views.PayableTypeServiceListView.as_view(), name='payables-type-service'),
]

    #path('', views.getData),
    #path('add/', views.addData),