from django.db import models

class Transactions(models.Model):
#choice for the type of transaction
    Type_choice = [
        ('expenses','Expenses'),
        ('icome', 'Income'),
    ]
    #create table / model fields to be stored in the database
    date = models.DateField(auto_now_add=True)
    Type = models.CharField(max_length=7, choices=Type_choice)
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return f"{self.Type} - {self.category} - {self.amount}"





        

# Create your models here.
