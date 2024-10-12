from django.urls import path
from .models import *
from .views import *

# Create your views here.
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', Index.as_view(), name='index'),
]