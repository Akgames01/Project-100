from django import forms

from .models import User,Login


class UserForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your Name',
        'id': 'Name1',
        'class': "form-control mb-2",
        'style': "width:10em;"
    }))
    UserID = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'UserId example:some1%43',
        'id': 'ID',
        'class': "form-control mb-2",
        'style': "width:10em;"
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*********',
        'id': 'pass',
        'class': "form-control mb-2",
        'style': "width:10em;"
    }))
    DOB = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'MM-DD-YYYY',
        'id': 'DOB',
        'class': "form-control mb-2",
        'style': "width:10em;"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'some123@example.com',
        'id': 'email',
        'class': "form-control mb-2",
        'style': "width:10em;"
    }))
    Phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        'style': "width:10em;"
    }))
    PlaceofBirth = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        'style': "width:10em;"
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
class LoginForm(forms.ModelForm):
    ID = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User ID',
        'id':'ID',
        'class':'form-control mb-2',
        'style':'width:10em;',
    
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id':'pass',
        'class':'form-control mb-2',
        'style':'width:10em;',
    }))
    class Meta:
        model = Login
        fields = [
            'ID',
            'password',
        ]
    

