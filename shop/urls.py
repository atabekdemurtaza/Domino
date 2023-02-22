from django.urls import path
from .views import *


urlpatterns = [
	path('', home, name='home'),

	path('all-products/', products, name='products'),
	path('all-products/product-<int:pk>/', product, name='products'),
	
]