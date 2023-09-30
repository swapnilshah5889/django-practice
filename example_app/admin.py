from django.contrib import admin
from example_app.models import BakedGood
from example_app.models import Car
# Register your models here.
admin.site.register(BakedGood)
admin.site.register(Car)