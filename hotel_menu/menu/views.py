from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .utils import generate_qr_code
from .models import Order, OrderItem, Breakfast, Tandoor_se, Main_course, Mushroom_se, Paneer_se, Snacks, Champ, Salad, Raita, Papad, Pulao_Rice, Dessert_cold_drinks
from .forms import CustomerInfoForm
from .utils import get_cart_count

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

def add_to_cart(request, item_type, item_id):
    item_model = {
        'breakfast': Breakfast,
        'tandoor': Tandoor_se,
        'main_course': Main_course,
        'mushroom': Mushroom_se,
        'paneer': Paneer_se,
        'snacks': Snacks,
        'champ': Champ,
        'salad': Salad,
        'raita': Raita,
        'papad': Papad,
        'pulao_rice': Pulao_Rice,
        'dessert_cold_drinks': Dessert_cold_drinks,
    }.get(item_type)

    item = get_object_or_404(item_model, id=item_id)

    cart = request.session.get('cart', {})
    item_key = f"{item_type}_{item_id}"

    if item_key in cart:
        cart[item_key]['quantity'] += 1
    else:
        cart[item_key] = {
            'item_type': item_type,
            'item_id': item_id,
            'quantity': 1,
            'name': item.name,
            'price': str(item.price)
        }

    request.session['cart'] = cart

    cart_count = sum(item['quantity'] for item in cart.values())

    return JsonResponse({'cart_count': cart_count})

def customer_info(request):
    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            request.session['customer_info'] = form.cleaned_data
            return redirect('place_order')
    else:
        form = CustomerInfoForm()
    return render(request, 'menu/customer_info.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('view_cart')

        customer_info = request.session.get('customer_info', {})
        if not customer_info:
            return redirect('customer_info')

        order = Order.objects.create(**customer_info)

        for item_key, item_data in cart.items():
            OrderItem.objects.create(
                order=order,
                item_type=item_data['item_type'],
                item_id=item_data['item_id'],
                quantity=item_data['quantity'],
                name=item_data['name'],
                price=item_data['price']
            )

        request.session['cart'] = {}
        request.session['customer_info'] = {}
        return redirect('order_success')

    return redirect('view_cart')

def order_success(request):
    return render(request, 'menu/order_success.html')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    return render(request, 'menu/cart.html', {'cart': cart, 'cart_count': cart_count})


def add_to_cart_ajax(request):
    item_type = request.POST.get('item_type')
    item_id = request.POST.get('item_id')

    # Assuming you have a way to add the item to the cart
    if item_type == 'breakfast':
        item = Breakfast.objects.get(id=item_id)
    elif item_type == 'tandoor':
        item = Tandoor_se.objects.get(id=item_id)
    elif item_type == 'main_course':
        item = Main_course.objects.get(id=item_id)
    elif item_type == 'mushroom':
        item = Mushroom_se.objects.get(id=item_id)
    elif item_type == 'paneer':
        item = Paneer_se.objects.get(id=item_id)
    elif item_type == 'snacks':
        item = Snacks.objects.get(id=item_id)
    elif item_type == 'champ':
        item = Champ.objects.get(id=item_id)
    elif item_type == 'salad':
        item = Salad.objects.get(id=item_id)
    elif item_type == 'raita':
        item = Raita.objects.get(id=item_id)
    elif item_type == 'papad':
        item = Papad.objects.get(id=item_id)
    elif item_type == 'pulao_rice':
        item = Pulao_Rice.objects.get(id=item_id)
    elif item_type == 'dessert_cold_drinks':
        item = Dessert_cold_drinks.objects.get(id=item_id)
    else:
        return JsonResponse({'error': 'Invalid item type'}, status=400)

    # Add item to the cart (implementation will vary)
    request.session['cart'] = request.session.get('cart', [])
    request.session['cart'].append(item_id)

    # Get updated cart count
    cart_count = get_cart_count(request)

    return JsonResponse({'cart_count': cart_count})