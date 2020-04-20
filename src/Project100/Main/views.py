from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate
from .forms import UserForm,LoginForm
def login_view(request,*args,**kwargs):
    my_form = UserForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = UserForm()
    context = {
        'form':my_form,
    }
    return render(request,'signup.html',context)
# Create your views here.
def main_view(request,*args,**kwargs):
    #K = User.objects.get()
    return render(request,'Main.html',{})
def Login_view(request,*args,**kwargs):
    Form = LoginForm(request.POST or None)
    if Form.is_valid():
        print(Form)
        user = authenticate(ID='rahul21',password='rahul123')
        
        
        
        #print(Form)
        if user is not None:
            Form = LoginForm()
            return redirect('userlogin/home')
            #print('main')
            #return render(request,'Main.html',{})
        
    
    context = {
        'form':Form,
    }
    return render(request,'login.html',context)
def about_page(request,*args,**kwargs):
    
    context = {
        'about_finance':"A financial market is a market in which people trade financial securities and derivatives at low transaction costs. Some of the securities include stocks and bonds, and precious metals. The term market is sometimes used for what are more strictly exchanges, organizations that facilitate the trade in financial securities, e.g., a stock exchange or commodity exchange. This may be a physical location (such as the NYSE, LSE, JSE, BSE) or an electronic system (such as NASDAQ). Much trading of stocks takes place on an exchange; still, corporate actions (merger, spinoff) are outside an exchange, while any two companies or people, for whatever reason, may agree to sell stock from the one to the other without using an exchange. Trading of currencies and bonds is largely on a bilateral basis, although some bonds trade on a stock exchange, and people are building electronic systems for these as well, to stock exchanges.",
        'about_us':'What we do is advice people what will be good for them',
    }
    return render(request,'MainPage.html',context)
def Finance(request,*args,**kwargs):
    context ={
        
    }