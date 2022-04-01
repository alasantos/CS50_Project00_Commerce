from pickle import TRUE
from tkinter import CASCADE
from typing_extensions import Required
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    pass

class Category( models.Model ):
    name = models.CharField(name='Name', max_length=64)
    description = models.TextField(name='Description')
    CreateDate = models.DateField(name='Createdate',default=date.today)
   # User = models.ForeignKey( User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.Name} : {self.Description} ({self.Createdate})"
        
class Item( models.Model ):
    title = models.CharField( name='Title', max_length=64)
    description = models.TextField( name='Description')
    ItemimageURL = models.CharField( name='ItemImage', max_length=128)
    startingBid = models.DecimalField( name='StartingBid', max_digits=8, decimal_places=2)
    categoryId = models.ForeignKey( Category, name='Category', null=True ,on_delete=models.SET_NULL, related_name="ItensPerCategory")
    userId = models.ForeignKey( User, name="User", on_delete= models.CASCADE, related_name="ItemsPerCategory", default=1)
    createDate = models.DateField(name="CreateDate", default=date.today)

    def __str__( self ):
        return f"({self.id}) - {self.Title} (price {self.startingBid}) "
