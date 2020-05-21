from django.shortcuts import render,redirect
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
)
# Create your views here.
def main_cover(request,*args,**kwargs):
    context ={
            'main':'Choose your stock'
    }
    return render(request,'Finance.html',{})