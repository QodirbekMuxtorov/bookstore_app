from django import forms
from .models import Book, Order


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'category', 'writer', 'image', 'file']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Narx 0 dan katta bo'lishi kerak.")
        return price


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'quantity']