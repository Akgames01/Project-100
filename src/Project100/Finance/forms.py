from django import forms


from .models import Stock


class StockForm(forms.ModelForm):
    Name = forms.CharField(widget = forms.TextInput(attrs = {
        
    }))