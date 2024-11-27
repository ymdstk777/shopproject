from django import forms
from .models import ShopPost

class ShopPostForm(forms.ModelForm):
    class Meta:
        model = ShopPost
        fields = ['category', 'title', 'description', 'price', 'condition', 'product_image']
