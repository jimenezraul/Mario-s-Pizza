from django.urls import path
from . import views
from django.conf.urls import url, include


app_name = 'pizzeria'

urlpatterns = [
    path('store/', views.store, name='store'),
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    path('contact_us/', views.contact_us, name='contect-us'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('sandwich-add-to-cart/<slug>/',
         views.sandwich_add_to_cart, name='sandwich-add-to-cart'),
    path('remove-from-cart/<id>/',
         views.remove_from_cart, name='remove-from-cart'),
    path('update_quantity_up/<id>/',
         views.update_quantity_up, name='update-quantity-up'),
    path('update_quantity_down/<id>/',
         views.update_quantity_down, name='update-quantity-down'),

]
