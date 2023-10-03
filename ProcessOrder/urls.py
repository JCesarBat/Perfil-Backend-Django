
from .views import order_processor
from django.urls import path

urlpatterns=[
    path('api/order',order_processor.as_view(),name='order')
]