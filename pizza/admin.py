from django.contrib import admin
from .models import Pizza, Order, OrderItem, Sandwiches

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Sandwiches)
