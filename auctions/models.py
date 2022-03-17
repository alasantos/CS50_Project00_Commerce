from pickle import TRUE
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    pass

class Category( models.Model ):
    Name = models.CharField(name='categoryName', max_length=64)
    Description = models.TextField(name='categoryDescription')
    CreateDate = models.DateField(name='categoryCreateDate',default=date.today)
   # User = models.ForeignKey( User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.categoryName} : {self.categoryDescription} ({self.categoryCreateDate})"

class Item( models.Model ):
    ShortDescription = models.CharField( name='ShortDescription', max_length=64)
    LongDescription = models.TextField( name='CompleteDescription')
    CategoryId = models.ForeignKey( Category, name='Category', null=TRUE ,on_delete=models.SET_NULL, related_name="ItensPerCategory")
    UserId = models.ForeignKey( User, name="User", on_delete= models.CASCADE, related_name="ItemsPerCategory", default=1)

    def __str__ ( self ):
        return f"Item description: {self.ShortDescription} - CategoryId: {self.Category}"
