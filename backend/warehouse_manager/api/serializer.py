from rest_framework import serializers
from .models import Client, Inventory, Sold_item

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class Sold_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sold_item
        fields = '__all__'