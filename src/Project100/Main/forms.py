from django import forms

from .models import User


class UserForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your Name',
        'id': 'Name1',
        'class': "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    UserID = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'UserId example:some1%43',
        'id': 'ID',
        'class': "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*********',
        'id': 'pass',
        'class': "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    DOB = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'MM-DD-YYYY',
        'id': 'DOB',
        'class': "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'some123@example.com',
        'id': 'email',
        'class': "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    Phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))
    PlaceofBirth = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        'style': "padding:10px;padding-left:5px;"
    }))

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
