from django.forms import fields
from .models import Product

from django import forms

class ProductForm(forms.ModelsForm):
    class Meta:
        model = Product
        fields = "__all__"








