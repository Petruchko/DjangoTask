from django.contrib import admin
from .models import Truck, TruckModel, TruckTrip

admin.site.register(Truck)
admin.site.register(TruckTrip)
admin.site.register(TruckModel)
