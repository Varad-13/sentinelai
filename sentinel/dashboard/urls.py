from django.urls import path
from .models import *
from .views import *

# Create your views here.
urlpatterns = [
    path('', Index.as_view(), name='index'),
]