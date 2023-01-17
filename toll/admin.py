from django.contrib import admin

# Register your models here.
from . models import Owner, Car

admin.site.register(Owner)
admin.site.register(Car)