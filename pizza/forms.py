from . import models
from django import forms


class PizzaForm(forms.ModelForm):

    class Meta:
        model = models.Pizza
        fields = ["crust_type", "size"]

class SandwichForm(forms.ModelForm):

    class Meta:
        model = models.Sandwiches
        fields = ["combo", "size"]

class ItemsForm(forms.ModelForm):

    class Meta:
        model = models.OrderItem
        fields = ["quantity"]
