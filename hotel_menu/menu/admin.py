# menu/admin.py

from django.contrib import admin
from .models import (
    Order, OrderItem, Breakfast, Tandoor_se, Main_course, Mushroom_se, Paneer_se, Snacks,
    Champ, Salad, Raita, Papad, Pulao_Rice, Dessert_cold_drinks
)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Breakfast)
admin.site.register(Tandoor_se)
admin.site.register(Main_course)
admin.site.register(Mushroom_se)
admin.site.register(Paneer_se)
admin.site.register(Snacks)
admin.site.register(Champ)
admin.site.register(Salad)
admin.site.register(Raita)
admin.site.register(Papad)
admin.site.register(Pulao_Rice)
admin.site.register(Dessert_cold_drinks)
