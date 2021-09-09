from django import forms

class CartAddFrom(forms.Form):
    quantity = forms.IntegerField(min_value=1,max_value=1)