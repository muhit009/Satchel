from typing import List
from django.urls import path
from product import views
from .views import ListProduct

urlpatterns = [
    path('',ListProduct.as_view(),name='Product')
    
]