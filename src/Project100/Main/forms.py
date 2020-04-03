from django import forms

from .models import User


class Form(forms.ModelForm):
    Name = forms.CharField(labels='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your Name',
        'id': 'Name1',
    }))
    UserID = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'UserId example:some1%43',
        'id': 'ID',
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*********',
        'id': 'pass',
    }))
    DOB = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'MM-DD-YYYY',
        'id': 'DOB',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'some123@example.com',
        'id': 'email',
    }))
    Phone = forms.CharField()
    PlaceofBirth = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'Name',
            'UserID',
            'Password',
            'DOB',
            'email',
            'Phone',
            'PlaceofBirth',
        ]
