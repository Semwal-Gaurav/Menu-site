from django import forms
from .models import Order, OrderItem, Breakfast, Tandoor_se, Main_course, Mushroom_se, Paneer_se, Snacks, Champ, Salad, Raita, Papad, Pulao_Rice, Dessert_cold_drinks

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone']

class OrderItemForm(forms.Form):
    menu_item = forms.ModelChoiceField(queryset=Breakfast.objects.all(), required=False)
    quantity = forms.IntegerField(min_value=1, required=False)
    
    def __init__(self, *args, **kwargs):
        menu_items = kwargs.pop('menu_items', Breakfast.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['menu_item'].queryset = menu_items
