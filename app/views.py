from unicodedata import category
from django import views
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# def home(request):
#  return render(request, 'app/home.html')    function based views
class ProductView(View):
 def get(self, request):
     bags = Product.objects.filter(category='B')
     jackets = Product.objects.filter(category='J')
     clay_utensils = Product.objects.filter(category='CL')
     duffles = Product.objects.filter(category='D')
     return render(request, 'app/home.html', {'bags': bags, 'jackets': jackets, 'clay_utensils': clay_utensils, 'duffles': duffles})


# def product_detail(request):
#  return render(request, 'al')
class ProductDetailView(View):
 def get(self, request, pk):
    product = Product.objects.get(pk=pk)
    item_already_in_cart = False

    itemalreadyincart = Cart.objects.filter(Q(product=
	product.id) & Q(user = request.user)).exists()
    return render(request, 'app/productdetail.html', {'product': product,'itemalreadyincart':itemalreadyincart})

def add_to_cart(request):
	user=request.user
	product_id=request.GET.get('prod_id')
	product=Product.objects.get(id=product_id)
	Cart(user=user,product=product).save()

	return redirect('/cart')


def show_cart(request):
	if request.user.is_authenticated:
		user=request.user
		cart=Cart.objects.filter(user=user)
		amount=0.0

		shipping_amount=70.0

		total_amount=0.0

		# cart_product=[p for p in Cart.objects.all() if p.user == user]
		cart_product=[]

		for p in Cart.objects.all():
			if p.user==user:
				cart_product.append(p)
				amount+=p.product.discounted_price*p.quantity+shipping_amount

		total_amount=amount

		print(cart_product)
		print(amount)


		context={
			'carts':cart,
			'amount':amount,
			'total':total_amount,
			'shipping':shipping_amount,
		}
		return render(request, 'app/addtocart.html',context)


def plus_cart(request):
	if request.method=="GET":
		prod_id=request.GET['prod_id']
		c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity+=1
		c.save()
		amount=0.0
		shipping_amount=70.0
		user=request.user
		cart_product=[p for p in Cart.objects.all() if p.user==user]

		for p in cart_product:
			tempamount=(p.quantity * p.product.discounted_price)
			amount+=tempamount
			

		data={
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount,
		}

		return JsonResponse(data) 

def minus_cart(request):
	if request.method=="GET":
		prod_id=request.GET['prod_id']
		c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity-=1
		c.save()
		amount=0.0
		shipping_amount=70.0
		user=request.user
		cart_product=[p for p in Cart.objects.all() if p.user==user]

		for p in cart_product:
			tempamount=(p.quantity * p.product.discounted_price)
			amount+=tempamount
		

		data={
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount,
		}

		return JsonResponse(data) 

def remove_cart(request):
	if request.method=="GET":
		prod_id=request.GET['prod_id']
		c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.delete()
		amount=0.0
		shipping_amount=70.0
		user=request.user
		cart_product=[p for p in Cart.objects.all() if p.user==user]

		for p in cart_product:
			tempamount=(p.quantity * p.product.discounted_price)
			amount+=tempamount
			

		data={
			'amount':amount,
			'totalamount':amount+shipping_amount,
		}

		return JsonResponse(data) 




def buy_now(request):
 return render(request, 'app/buynow.html')


def profile(request):
 return render(request, 'app/profile.html')



def address(request):
	add=Customer.objects.filter(user=request.user)
	context={
		'address':add,
		'active':'btn-primary',
	}
	return render(request, 'app/address.html',context)


def orders(request):
	op=OrderPlaced.objects.filter(user=request.user)
	context={
		'order_placed':op,
	}

	return render(request,'app/orders.html',context)



def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='B')
    elif data == 'adidas' or data == 'dalix':
         mobiles = Product.objects.filter(category='B').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='B').filter(discounted_price__lt=5000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='B').filter(discounted_price__gt=5000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def topwear(request, data=None):
	context = {}
	if data == None:
		topwears = Product.objects.filter(category='J')

	elif data == 'Puma' or data == 'Roadster':
		topwears = Product.objects.filter(category='J').filter(brand=data)
	elif data == 'below':
		topwears = Product.objects.filter(
		    category='J').filter(discounted_price__lt=5000)
	elif data == 'above':
		topwears = Product.objects.filter(
		    category='J').filter(discounted_price__gt=5000)
	context = {
			'topwears': topwears
		}
	return render(request, 'app/topwear.html', context)


def bottomwear(request, data=None):
	context = {}
	if data == None:
		bottomwears = Product.objects.filter(category='CL')
    
	elif data == 'Spykar' or data == 'Lee':
		bottomwears = Product.objects.filter(category='CL').filter(brand=data)
	elif data == 'below':
		bottomwears = Product.objects.filter(
		    category='CL').filter(discounted_price__lt=500)

	elif data == 'above':
		bottomwears = Product.objects.filter(
		    category='CL').filter(discounted_price__gt=500)
	context = {
			'bottomwears': bottomwears
		}
	return render(request, 'app/bottomwear.html', context)


# def login(request):
#  return render(request, 'app/login.html')


def checkout(request):
	user=request.user
	add=Customer.objects.filter(user=user)
	cart_items=Cart.objects.filter(user=user)

	amount=0.0
	shipping_amount=70.0
	totalamount=0.0

	user=request.user
	cart_product=[p for p in Cart.objects.all() if p.user==user]

	for p in cart_product:
		tempamount=(p.quantity * p.product.discounted_price)
		amount+=tempamount

	totalamount=amount+shipping_amount

	context={
		'address':add,
		'total':totalamount,
		'carts':cart_items,
	}
	return render(request, 'app/checkout.html',context)

def payment_done(request):
	user=request.user
	custid=request.GET.get('custid')
	customer=Customer.objects.get(id=custid)
	cart=Cart.objects.filter(user=user)
	for c in cart:
		OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
		c.delete() 
	return redirect("orders")

# def customerregistration(request):
#  return render(request, '')


class CustomerRegistrationView(View):

	def get(self,request):
		form=CustomerRegistrationForm()
		context={
			'form':form
		}
		return render(request, 'app/customerregistration.html',context)
	def post(self,request):
		form=CustomerRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,"Congratulations!! Registered Successfully")
			form.save()
		context={
			'form':form
		}
		return render(request, 'app/customerregistration.html',context)



class Profileview(View):
	def get(self,request):
		form=CustomerProfileForm()
		context={
			'form':form,
			'active':'btn-primary',
		}
		return render(request,'app/profile.html',context)
	def post(self,request):
		form=CustomerProfileForm(request.POST)
		if form.is_valid():
			usr=request.user
			name=form.cleaned_data['name']
			locality=form.cleaned_data['locality']
			city=form.cleaned_data['city']
			state=form.cleaned_data['state']
			zipcode=form.cleaned_data['zipcode']

			reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)

			reg.save()

			messages.success(request,'Congratulations!! Profile Updated Successfully')
		context={
			'form':form,
			'active':'btn-primary',
		}
		return render(request,'app/profile.html',context)