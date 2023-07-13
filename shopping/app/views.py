from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


# def add_to_cart(request):
#     return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-secondary'})


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        laptop = Product.objects.filter(category='L')
        mobile = Product.objects.filter(category='M')
        beauryitem = Product.objects.filter(category='BI')
        electronicitem = Product.objects.filter(category='ELE')
        watch = Product.objects.filter(category='W')
        bag = Product.objects.filter(category='B')
        return render(request, 'app\home.html', {
            'topwear': topwear, 'mobile': mobile, 'laptop': laptop, 'bottomwear': bottomwear, 'bags': bag, 'beautyproduct': beauryitem, 'electronic': electronicitem, 'watch': watch,
        })


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
            return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart})
        else:
            return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart})


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Apple' or data == 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(category='L')
    elif data == 'Asus' or data == 'Apple':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__lt=75000)
    elif data == 'above':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__gt=75000)
    return render(request, 'app/laptop.html', {'laptops': laptops})


def topwear(request, data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'zara' or data == 'Nike':
        topwears = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__lt=700)
    elif data == 'above':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__gt=700)
    return render(request, 'app/topwear.html', {'topwears': topwears})


def bottomwear(request, data=None):
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'zara' or data == 'Nike':
        bottomwears = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__lt=1000)
    elif data == 'above':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__gt=1000)
    return render(request, 'app/bottomwear.html', {'bottomwears': bottomwears})


def bueatyproduct(request, data=None):
    if data == None:
        bueatyproduct = Product.objects.filter(category='BI')
    elif data == 'Lakme' or data == 'Maybelline':
        bueatyproduct = Product.objects.filter(
            category='BI').filter(brand=data)
    elif data == 'below':
        bueatyproduct = Product.objects.filter(
            category='BI').filter(discounted_price__lt=5000)
    elif data == 'above':
        bueatyproduct = Product.objects.filter(
            category='BI').filter(discounted_price__gt=5000)
    return render(request, 'app/bueatyitem.html', {'bueatyitem': bueatyproduct})


def electronicitem(request, data=None):
    if data == None:
        electronicitem = Product.objects.filter(category='ELE')
    elif data == 'samsung' or data == 'Boat':
        electronicitem = Product.objects.filter(
            category='ELE').filter(brand=data)
    elif data == 'below':
        electronicitem = Product.objects.filter(
            category='ELE').filter(discounted_price__lt=25000)
    elif data == 'above':
        electronicitem = Product.objects.filter(
            category='ELE').filter(discounted_price__gt=25000)
    return render(request, 'app/electronicitem.html', {'electronicitem': electronicitem})


def watch(request, data=None):
    if data == None:
        watch = Product.objects.filter(category='W')
    elif data == 'boat':
        watch = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'below':
        watch = Product.objects.filter(
            category='W').filter(discounted_price__lt=10000)
    elif data == 'above':
        watch = Product.objects.filter(
            category='W').filter(discounted_price__gt=10000)
    return render(request, 'app/watch.html', {'watch': watch})


def bags(request, data=None):
    if data == None:
        bags = Product.objects.filter(category='B')
    elif data == 'Caprese' or data == 'Lavie':
        bags = Product.objects.filter(category='B').filter(brand=data)
    elif data == 'below':
        bags = Product.objects.filter(
            category='B').filter(discounted_price__lt=5000)
    elif data == 'above':
        bags = Product.objects.filter(
            category='B').filter(discounted_price__gt=5000)
    return render(request, 'app/bags.html', {'bags': bags})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app\customerregistration.html', {'form ': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "congratulations ! Registered Successfully")
            form.save()
        return render(request, 'app\customerregistration.html', {'form': form})


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app\profile.html', {'form': form, 'active': 'btn-secondary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, "congratulations .. profile updated successfully")
        return render(request, 'app\profile.html', {'form': form, 'active': 'btn-secondary'})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discounted_price)
                amount += tempamount
                total_amount = amount+shipping_amount
            return render(request, 'app/addtocart.html', {'carts': cart, 'total_amount': total_amount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
