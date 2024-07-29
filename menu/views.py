from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import os
from .utils import generate_qr_code
from .models import Breakfast, Tandoor_se, Main_course, Mushroom_se, Paneer_se, Snacks, Champ, Salad, Raita, Papad, Pulao_Rice, Dessert_cold_drinks,Order, OrderItem
from .forms import OrderForm, OrderItemForm

def qr_code_view(request):
    qr_code_path = generate_qr_code('http://127.0.0.1:8000/menu/', 'menu_qr_code.png')
    with open(qr_code_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/png")
    



def menu_view(request):
    breakfast_items = Breakfast.objects.all()
    tandoor_items = Tandoor_se.objects.all()
    main_courses = Main_course.objects.all()
    mushroom_items = Mushroom_se.objects.all()
    paneer_items = Paneer_se.objects.all()
    snacks_items = Snacks.objects.all()
    champ_items = Champ.objects.all()
    salad_items = Salad.objects.all()
    raita_items = Raita.objects.all()
    papad_items = Papad.objects.all()
    pulao_rice_items = Pulao_Rice.objects.all()
    dessert_cold_drinks = Dessert_cold_drinks.objects.all()

    return render(request, 'menu/menu.html', {
        'breakfast_items': breakfast_items,
        'tandoor_items': tandoor_items,
        'main_courses': main_courses,
        'mushroom_items': mushroom_items,
        'paneer_items': paneer_items,
        'snacks_items': snacks_items,
        'champ_items': champ_items,
        'salad_items': salad_items,
        'raita_items': raita_items,
        'papad_items': papad_items,
        'pulao_rice_items': pulao_rice_items,
        'dessert_cold_drinks': dessert_cold_drinks,
    })



def order_create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        item_form = OrderItemForm(request.POST, menu_items=Breakfast.objects.all())
        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save()
            menu_item = item_form.cleaned_data['menu_item']
            quantity = item_form.cleaned_data['quantity']
            if menu_item and quantity:
                OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            return redirect('order_success')
    else:
        order_form = OrderForm()
        item_form = OrderItemForm(menu_items=Breakfast.objects.all())
    return render(request, 'menu/order_form.html', {'order_form': order_form, 'item_form': item_form})

def order_success(request):
    return render(request, 'menu/order_success.html')