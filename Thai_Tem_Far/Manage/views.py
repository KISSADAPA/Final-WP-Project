from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from Order.models import Buy
from Manage.models import Product

# Create your views here.

@login_required
def dashboard(request):
    context = {}
    Buys = Buy.objects.all().order_by('-id')
    context['Buys'] = Buys
    if request.method == 'POST':
        details = int(request.POST.get('details'))
        buyal = Buy.objects.get(pk=details)
        context['details'] = buyal
    return render(request, 'Manage/dashboard.html', context=context)

@login_required
def buy_approve(request, id_buy):
    buy_order = Buy.objects.get(pk=id_buy)
    buy_order.status = 'Approved'
    buy_order.save()
    return redirect('dashboard')

@login_required
def buy_deniel(request, id_buy):
    buy_order = Buy.objects.get(pk=id_buy)
    buy_order.status = 'Denied'
    buy_order.save()
    return redirect('dashboard')

@login_required
def product_hide(request, id_product):
    product = Product.objects.get(pk=id_product)
    product.status = 'HIDE'
    product.save()
    return redirect('product_dashboard')

@login_required
def product_unhide(request, id_product):
    product = Product.objects.get(pk=id_product)
    product.status = 'AVAILABLE'
    product.save()
    return redirect('product_dashboard')

@login_required
def home_product_hide(request, id_product):
    product = Product.objects.get(pk=id_product)
    product.status = 'HIDE'
    product.save()
    return redirect('homepage')

@login_required
def notavailable(request, id_buy):
    buy = Buy.objects.get(pk=id_buy)
    product = Product.objects.get(pk=buy.product_id.id)
    product.status = 'NO_AVAILABLE'
    product.save()
    return redirect('dashboard')

@login_required
def available(request, id_buy):
    buy = Buy.objects.get(pk=id_buy)
    product = Product.objects.get(pk=buy.product_id.id)
    product.status = 'AVAILABLE'
    product.save()
    return redirect('dashboard')

@login_required
def product_dashboard(request):
    context = {}
    available = []
    not_available = []
    hidden = []
    products = Product.objects.all()
    for product in products:
        if product.status == 'AVAILABLE':
            available.append(product)
        elif product.status == 'NO_AVAILABLE':
            not_available.append(product)
        elif product.status == 'HIDE':
            hidden.append(product)
    if len(available): context['available'] = available
    if len(not_available): context['not_available'] = not_available
    if len(hidden): context['hidden'] = hidden

    return render(request, 'Manage/addon.html', context=context)

