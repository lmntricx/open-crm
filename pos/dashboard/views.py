import datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from login.models import Users
from .models import Products, Orders, Customers
from .methods import method
from django.views.decorators.csrf import csrf_exempt


#Views here
def dash(request):
    products = Products.objects.all().values()
    customers = Customers.objects.all().values()
    orders = Orders.objects.all().values()
    users = Users.objects.all().values()

    template = loader.get_template('dashboard.html')
    context = {
        'Users': users,
        'products': products,
        'customers': customers,
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def newOrder(request):
    products = Products.objects.all().values()
    customers = Customers.objects.all().values()
    orders = Orders.objects.all().values()

    if request.method == 'POST':
        # Retrieve data from the submitted form
        CustomerId = request.POST.get('customerId')
        ProductId = request.POST.get('productId')
        datum = datetime.date.today()
        qty = request.POST.get('qty')

        results = method.createOrder(CustomerId, ProductId, datum, 0, qty)

    context = {
        'products': products,
        'customers': customers,
        'orders': orders,
    }
    print("Got here hebrhevr")
    print(" If there be any:"+str(orders))

    template = loader.get_template("createorder.html")
    return HttpResponse(template.render(context, request))


@csrf_protect
def newCustomer(request):
    customers = Customers.objects.all().values()

    if request.method == 'POST':
        # Retrieve data from the submitted form
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        street = request.POST.get('street')
        town = request.POST.get('town')
        city = request.POST.get('city')
        postalcode = request.POST.get('postalcode')

        results = method.insert_customer(customers,name,lastName,phone,email,street,town,city, postalcode )
        return HttpResponseRedirect('/dashboard/newcustomer')

    context = {
        'customers': customers,
    }

    template = loader.get_template("newcustomer.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def products(request):
    products = Products.objects.all().values()

    if request.method == 'POST':
        # Retrieve data from the submitted form
        name = request.POST.get('name')
        price = request.POST.get('price')
        datum = datetime.date.today()
        distributor = request.POST.get('distributor')

        results = method.insert_product(products, name, price, datum, distributor)
        return HttpResponseRedirect('/dashboard/products')
    context = {
        'products': products,
    }

    template = loader.get_template("products.html")
    return HttpResponse(template.render(context, request))


def product_delete(request, product_id):
    # Retrieve the product with the specified ID
    product = get_object_or_404(Products, product_id=product_id)

    product.delete()
    return HttpResponseRedirect('/dashboard/products')

def orders(request):
    orders = Orders.objects.all().values()
    template = loader.get_template("orders.html")
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


def employees(request):
    template = loader.get_template("employees.html")
    return HttpResponse(template.render())


