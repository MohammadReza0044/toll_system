from django.contrib import admin

# Register your models here.
from . models import Owner, Car , Traffic , Road

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Traffic)
admin.site.register(Road)