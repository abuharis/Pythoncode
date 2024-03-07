from django.db import models
from dataclasses import dataclass

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    id=models.CharField(max_length=200,primary_key=True)


class SalesSubmission(models.Model):
    number = models.CharField(max_length=100)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sales Submission {self.id}: {self.item} - {self.quantity}"

@dataclass
class Destinations():
    name: str
    id: int
    price: int

