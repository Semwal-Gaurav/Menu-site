from django.urls import path
from  . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('qr/', views.qr_code_view, name='qr_code'),
    path('add-to-cart/<str:item_type>/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
    path('customer_info/', views.customer_info, name='customer_info'), 
    path('add_to_cart_ajax/', views.add_to_cart_ajax, name='add_to_cart_ajax'),
]