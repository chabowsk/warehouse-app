from django.db import models
import datetime

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20) 
    surname = models.CharField(max_length=20) 
    phone = models.IntegerField()


    def __str__(self):
        return  self.name
    
class Stored_place(models.Model):
    GARAGE = "GARAZ"
    STORE = "STORE"
    Place = {
        GARAGE : "GARAZ",
        STORE : "STORE"
    }
    name = models.CharField(choices=Place, default=GARAGE)
    rack = models.CharField(max_length=5)
    shelf = models.CharField(max_length=5)
    case = models.CharField(max_length=5)
     
    def __str__(self):
        return  self.name
    
class Inventory(models.Model):
    
    ORDERED = "ZAMOWIONE"
    AVAILABLE = "DOSTEPNY"
    SOLD = "SPRZEDANY"
    InventoryStatus = {
        ORDERED: 'ZAMOWIONE',
        AVAILABLE: 'DOSTEPNY',
        SOLD: 'SPRZEDANY',
    }


    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=1000) 
    OEM_number = models.CharField(max_length=40)
    price = models.FloatField()
    #stored_at = models.ForeignKey(Stored_place, on_delete=models.CASCADE)
    #photo = models.ImageField(blank=True)
    status = models.CharField(choices=InventoryStatus, default=ORDERED)

    def __str__(self):
        return  self.name

class Sold_item(models.Model):
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.item


