from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Inventory, Sold_item
from .serializer import ClientSerializer, InventorySerializer, Sold_itemSerializer


#client
@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request,pk):
    try: 
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#inventory
@api_view(['GET'])
def get_inventories(request):
    inventories = Inventory.objects.all()
    serializer = InventorySerializer(inventories, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def create_inventory(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#sold item
@api_view(['GET'])
def get_sold_items(request):
    sold_items = Sold_item.objects.all()
    serializer = Sold_itemSerializer(sold_items, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def create_sold_item(request):
    serializer = Sold_itemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)