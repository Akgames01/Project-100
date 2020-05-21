from django.urls import path
from . import views
from .views import main_cover
urlpatterns=[
    path('Finance/',main_cover,name='Finance-cover'),
]