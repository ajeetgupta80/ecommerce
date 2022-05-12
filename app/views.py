from unicodedata import category
from django import views
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced


# def home(request):
#  return render(request, 'app/home.html')    function based views
class ProductView(View):
 def get(self, request):
     bags = Product.objects.filter(category='B')
     jackets = Product.objects.filter(category='J')
     clay_utensils = Product.objects.filter(category='CL')
     duffles = Product.objects.filter(category='D')
     return render(request,'app/home.html', { 'bags': bags, 'jackets': jackets , 'clay_utensils': clay_utensils, 'duffles': duffles})


# def product_detail(request):
#  return render(request, 'al')
class ProductDetailView(View):
 def get(self, request, pk):
     product = Product.objects.get(pk=pk)
     return render(request,'app/productdetail.html' ,{'product': product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
