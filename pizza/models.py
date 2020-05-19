from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse
from autoslug import AutoSlugField


class Pizza(models.Model):

    CRUST_TYPE = [
        ("Hand Tossed Pizza", "Hand Tossed Pizza"),
        ("Thin 'N Crispy", "Thin 'N Crispy"),
        ("Original Pan", "Original Pan"),
        ("Original Stuffed Crust", "Original Stuffed Crust"),
    ]

    TOPPINGS_CHOICES = [
        ("Cheese", "Cheese"),
        ("Pepperoni", "Pepperoni"),
        ("Hawiian", "Hawiian"),
        ("MeatLovers", "MeatLovers")
    ]

    SIZE_CHOICES = [
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    topping = 1.99

    name = models.CharField(max_length=30)
    crust_type = models.CharField(
        max_length=30, choices=CRUST_TYPE, default="Hand Tossed Pizza")
    slug = AutoSlugField(populate_from='name')
    toppings = models.CharField(max_length=30, choices=TOPPINGS_CHOICES)
    size = models.CharField(
        max_length=30, choices=SIZE_CHOICES, default="Medium")
    price = models.DecimalField(decimal_places=2, max_digits=6, default=8.99)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("pizzeria:add-to-cart", kwargs={
            'slug': self.slug
        })


class Sandwiches(models.Model):

    COMBO = [
        ("Meal", "Meal"),
        ("Sandwich", "Sandwich"),
    ]

    SIZE_CHOICES = [
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(max_length=30)
    combo = models.CharField(
        max_length=30, choices=COMBO, default="Meal")
    slug = AutoSlugField(populate_from='name')
    size = models.CharField(
        max_length=30, choices=SIZE_CHOICES, default="Medium")
    price = models.DecimalField(decimal_places=2, max_digits=6, default=8.99)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("pizzeria:sandwich-add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("pizzeria:sandwich-remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_update_up(self):
        return reverse("pizzeria:sandwich-update-quantity-up", kwargs={
            'slug': self.slug
        })

    def get_update_down(self):
        return reverse("pizzeria:sandwich-update-quantity-down", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    SIZE_CHOICES = [
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    pizza = models.ForeignKey(
        Pizza, blank=True, null=True, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(
        Sandwiches, blank=True, null=True, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=30, choices=SIZE_CHOICES, default="Medium")
    crust = models.CharField(max_length=30, blank=True)
    combo = models.CharField(max_length=30, blank=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def get_price(self):
        if self.size == "Small":
            self.price = 6.99
        elif self.size == "Medium":
            self.price = 8.99
        else:
            self.price = 10.99
        return self.price

    def __str__(self):
        if self.pizza:
            item = f"{self.quantity} {self.size} {self.crust} {self.pizza.name} {self.get_total_price()}"
        else:
            item = f"{self.quantity} {self.size} {self.combo} {self.sandwich.name} {self.get_total_price()}"
        return item

    def get_total_price(self):
        if self.pizza:
            if self.pizza.toppings == "Cheese":
                return self.quantity * self.get_price()
            else:
                toppings_price = self.quantity * self.pizza.topping
                return self.quantity * self.get_price() + toppings_price
        else:
            return self.quantity * self.get_price()

    def get_update_up(self):
        return reverse("pizzeria:update-quantity-up", kwargs={
            'id': self.id
        })

    def get_update_down(self):
        return reverse("pizzeria:update-quantity-down", kwargs={
            'id': self.id
        })

    def get_remove_from_cart_url(self):
        return reverse("pizzeria:remove-from-cart", kwargs={
            'id': self.id
        })


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Total: ${self.get_total()}"

    def get_delivery(self):
        if self.items.count() >= 1:
            delivery_price = 5.00
        else:
            delivery_price = 0.00
        return delivery_price

    def get_tax(self):
        tax = 0.06
        total = self.get_sub_total()
        total *= tax
        return total

    def get_sub_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_price()
        return total

    def get_total(self):
        sub_total = self.get_sub_total()
        tax = self.get_tax()
        delivery = self.get_delivery()
        total = sub_total + tax + delivery
        return total
