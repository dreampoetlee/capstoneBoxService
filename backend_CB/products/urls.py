from django.urls import URLPattern, path

import products
from . views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug>', ProductDetailView.as_view(), name='detail')
]
