from django.urls import path
from .views import get_clients, create_client, client_detail, get_inventories, create_inventory, get_sold_items, create_sold_item#, item_detail

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
    path('clients/create', create_client, name='create_client'),
    path('clients/<int:pk>', client_detail, name='client_detail'),
    path('inventory/', get_inventories, name='get_inventories'),
    path('inventory/create', create_inventory, name='create_inventory'),
    path('sold_items/', get_sold_items, name='get_sold_items'),
    path('sold_items/create', create_sold_item, name='create_sold_item'),
    #path('items/<int:pk>', item_detail, name='item_detail')
]