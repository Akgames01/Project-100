from django.urls import path
from . import views
#from .views import Login_view,main_view
urlpatterns=[
path('userlogin/',views.Login_view,name='login'),
path('userlogin/home/',views.main_view,name='main-home'),
path('Main/',views.about_page,name='about-page')
]