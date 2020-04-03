from django.shortcuts import render
from .models import User
from .forms import UserForm
def login_view(request,*args,**kwargs):
    my_form = UserForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = UserForm()
    context = {
        'form':my_form,
    }
    return render(request,'login.html',context)
# Create your views here.
