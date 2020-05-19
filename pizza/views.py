from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem, Pizza, Sandwiches
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PizzaForm, ItemsForm, SandwichForm


def store(request):

    context = {
        "home": "active"
    }
    return render(request, "pizza/index.html", context)


@login_required(login_url='register')
def cart(request):
    order = Order.objects.filter(user=request.user)
    items = []
    form = PizzaForm()
    itemsform = ItemsForm()
    pizza_choice = Pizza.objects.all()
    if order:
        order = order[0]
        items = order.items.all()
    context = {
        "cart": "active",
        "order": order,
        "items": items,
        "itemsform": itemsform,
    }
    return render(request, "pizza/cart.html", context)


def contact_us(request):

    order = Order.objects.filter(user=request.user)
    items = []

    if order:
        order = order[0]
        items = order.items.all()
    context = {
        "order": order,
        "items": items,
        "contactus": "active"
    }

    return render(request, "pizza/contactus.html", context)


@login_required(login_url='register')
def order(request):
    order = Order.objects.filter(user=request.user)
    items = []
    form = PizzaForm()
    sandwich_form = SandwichForm()
    pizza_choice = Pizza.objects.all()
    sandwich_choice = Sandwiches.objects.all()

    if order:
        order = order[0]
        items = order.items.all()
    context = {
        "order": order,
        "items": items,
        "p_order": "active",
        "form": form,
        "pizza_choice": pizza_choice,
        "sandwich_form": sandwich_form,
        "sandwich_choice": sandwich_choice,
    }

    return render(request, "pizza/order.html", context)


@login_required(login_url='register')
def add_to_cart(request, slug):
    item = get_object_or_404(Pizza, slug=slug)
    if OrderItem.objects.filter(user=request.user).count() == 0:
        order_item, created = OrderItem.objects.get_or_create(
            pizza=item,
            user=request.user,
            ordered=False
        )
    else:
        order_item = OrderItem.objects.all()

    if request.method == 'POST':
        crust = request.POST['crust_type']
        size = request.POST['size']

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pizza__slug=item.slug).exists():
            if order.items.filter(pizza__slug=item.slug, crust=crust, size=size).exists():
                order_item = order.items.filter(
                    pizza__slug=item.slug, crust=crust, size=size)
                order_item = order_item[0]
                order_item.quantity += 1
                order_item.save()
                messages.success(request, "This item quantity was updated.")
                return redirect("pizzeria:order")
            else:
                # if the item is in order but crust and size don't mach the one in qs, will create a new one
                order.items.create(user=request.user, pizza=item)
                order_item = order.items.filter(
                    pizza__slug=item.slug)
                order_item = order_item.last()
                order_item.size = size
                order_item.crust = crust
                order_item.save()
                messages.success(request, "This item was added to your order.")
                return redirect("pizzeria:order")

        else:
            order_item, created = OrderItem.objects.get_or_create(
                pizza=item,
                user=request.user,
                ordered=False
            )
            order.items.add(order_item)
            order_item.size = size
            order_item.crust = crust
            order_item.save()
            messages.success(request, "This item was added to your order.")
            return redirect("pizzeria:order")
    else:
        # Creating a new order
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        # check for crust and pizza size to add to the order or it will take the default values
        order_item.size = size
        order_item.crust = crust
        order_item.save()
        messages.success(request, "This item was added to your order.")
        return redirect("pizzeria:order")


@login_required(login_url='register')
def sandwich_add_to_cart(request, slug):
    item = get_object_or_404(Sandwiches, slug=slug)
    if OrderItem.objects.filter(user=request.user).count() == 0:
        order_item, created = OrderItem.objects.get_or_create(
            sandwich=item,
            user=request.user,
            ordered=False
        )
    else:
        order_item = OrderItem.objects.all()

    if request.method == 'POST':
        combo = request.POST['combo']
        size = request.POST['size']

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(sandwich__slug=item.slug).exists():
            if order.items.filter(sandwich__slug=item.slug, combo=combo, size=size).exists():
                order_item = order.items.filter(
                    sandwich__slug=item.slug, combo=combo, size=size)
                order_item = order_item[0]
                order_item.quantity += 1
                order_item.save()
                messages.success(request, "This item quantity was updated.")
                return redirect("pizzeria:order")
            else:
                # if the item is in order but crust and size don't mach the one in qs, will create a new one
                order.items.create(user=request.user, sandwich=item)
                order_item = order.items.filter(
                    sandwich__slug=item.slug)
                order_item = order_item.last()
                order_item.size = size
                order_item.combo = combo
                order_item.save()
                messages.success(request, "This item was added to your order.")
                return redirect("pizzeria:order")

        else:
            order_item, created = OrderItem.objects.get_or_create(
                sandwich=item,
                user=request.user,
                ordered=False
            )
            order.items.add(order_item)
            order_item.size = size
            order_item.combo = combo
            order_item.save()
            messages.success(request, "This item was added to your order.")
            return redirect("pizzeria:order")
    else:
        # Creating a new order
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        # check for crust and pizza size to add to the order or it will take the default values
        order_item.size = size
        order_item.combo = combo
        order_item.save()
        messages.success(request, "This item was added to your order.")
        return redirect("pizzeria:order")


@login_required(login_url='register')
def remove_from_cart(request, id):
    item = OrderItem.objects.filter(pk=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pk=id).exists():
            order_item = OrderItem.objects.filter(
                pk=id,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from your cart.")
            return redirect("pizzeria:cart")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("pizzeria:cart")
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("pizzeria:cart")


@login_required(login_url='register')
def update_quantity_up(request, id):
    item = OrderItem.objects.filter(pk=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pk=id).exists():
            order_item = OrderItem.objects.filter(
                pk=id,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.success(request, "Quantity has been updated.")
                return redirect("pizzeria:cart")
            else:
                order_item.delete()
                messages.warning(
                    request, "This item was removed from your cart.")
                return redirect("pizzeria:cart")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("pizzeria:cart")
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("pizzeria:cart")


@login_required(login_url='register')
def update_quantity_down(request, id):
    item = OrderItem.objects.filter(pk=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pk=id).exists():
            order_item = OrderItem.objects.filter(
                pk=id,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.success(request, "Quantity has been updated.")
                return redirect("pizzeria:cart")
            else:
                order_item.delete()
                messages.warning(
                    request, "This item was removed from your cart.")
                return redirect("pizzeria:cart")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("pizzeria:cart")
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("pizzeria:cart")
