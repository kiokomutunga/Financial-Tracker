from django.db import models
from django.contrib.auth.models import User

class Transactions(models.Model):
#choice for the type of transaction
    Type_choice = [
        ('expenses','Expenses'),
        ('icome', 'Income'),
    ]
    #create table / model fields to be stored in the database
    date = models.DateField(auto_now_add=True)
    Type = models.CharField(max_length=100, choices=Type_choice)
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return f"{self.Type} - {self.category} - {self.amount}"

class Budget(models.Model):
    CATEGORY_CHOICE = [
        ('Food','Food'),
        ('Transport','Transport'),
        ('Housing','Housing'),
        ('Entertainment','Entertainment'),
        ('Other','Other'),
    ]

    #tables model and tables
    Category = models.CharField(max_length=100,choices=CATEGORY_CHOICE)
    amount = models.FloatField()
    month = models.DateTimeField()
    year = models.DateTimeField() 


    def __str__(self):
        return f"{self.category} - {self.month}/{self.year} - {self.amount}"




        

# Create your models here.
