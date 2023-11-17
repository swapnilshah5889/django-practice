from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class BakedGood(models.Model): 
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.CharField(
        max_length=2,
        choices=[
            ('BG',"Bagel"),
            ('BR',"Bread"),
            ('CO',"Cookie"),
            ('CA',"Cake"),
            ('PR',"Pretzel")
        ]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    recipe = models.TextField()
    baked_on = models.DateTimeField()

    def to_json(self):
        return {
            "name":self.name,
            "desc":self.desc,
            "good_type":self.good_type,
            "price":self.price,
            "recipe":self.recipe
        }

class Car(models.Model):
    CAR_BRANDS = [  
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Acura', 'Acura'),
        ('Nissan', 'Nissan'),
    ]

    make = models.CharField(max_length=50, choices=CAR_BRANDS)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(max_length=4, validators=[MinLengthValidator(4)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, blank=True, null=True)
    mileage = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def to_json(self):
        return {
            "make":self.make,
            "model":self.model,
            "year":self.year,
            "price":self.price,
            "color":self.color,
            "mileage":self.mileage,
            "description":self.description
        }
