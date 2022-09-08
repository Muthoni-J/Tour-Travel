from django.shortcuts import render
from tour.models import Tour
from . import 


def register_customers(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customers.html",
                  {"form":form})
# Create your views here.
