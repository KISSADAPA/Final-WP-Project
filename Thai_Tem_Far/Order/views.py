from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Q

from datetime import datetime

from Manage.models import Product, Promo
from Order.models import Buy

from Order.forms import add_product

# Create your views here.

@login_required
def booking(request, id_product):
    context = {}
    product = Product.objects.get(pk=id_product)
    price = 0
    day = 0
    promotion_info = None
    if request.method == 'POST':
        discount = 0
        start_date = request.POST.get('start_date')
        stop_date = request.POST.get('end_date')
        promotion = request.POST.get('promotion_code')
        is_submit = request.POST.get('is_submit')

        context['start_date'] = start_date
        context['end_date'] = stop_date
        context['promotion'] = promotion
              
       
        #date converter form 
        if(start_date and stop_date):
            date_format = "%Y/%m/%d %H:%M"

            a = datetime.strptime(start_date, date_format)
            b = datetime.strptime(stop_date, date_format)


            delta = b - a
            print('amount day : ', delta.days)
            print('amount pay : ', delta.days*product.price)
            
            price = delta.days*product.price
            day = delta.days
            if day < 0:
                context['promo_error'] = 'กรุณาเลือกวันที่สั่งซื้อให้ถูกต้อง'
                context['not_accept'] = 'not_accept'
            
        
        if not (start_date or stop_date):
            context['promo_error'] = 'โปรดกรอกวันที่ให้ถูกต้อง'
            print('โปรดกรอกวันที่ให้ถูกต้อง')
            context['not_accept'] = 'not_accept'


        # promotion check code
        if len(promotion) == 0:
            pass
            promotion_info = None
        else:
            try:
                promotion_info = Promo.objects.get(promotion_code=promotion)
            except Promo.DoesNotExist:
                promotion_info = None
            if promotion_info:
                print(promotion_info.expire_day)
                print(datetime.now())

                expire = str(promotion_info.expire_day).replace('-','/')
                now = str(datetime.now()).replace('-','/')

                print(expire[:16])
                print(now[:16])

       
                c = datetime.strptime(expire[:16], date_format)
                d = datetime.strptime(now[:16], date_format)

                delta2 = c-d
                day_left = delta2.days

                if price < promotion_info.minimum_cost:
                    context['promo_error'] = 'ใช้โค้ดไม่สำเร็จ ราคาไม่ถึงขั้นต่ำที่กำหนด'
                elif day_left <= 0:
                    context['promo_error'] = 'ใช้โค้ดไม่สำเร็จ โค้ดหมดเวลา'
                else:
                    promo_cost = price*(promotion_info.discount_percent/100)
                    price = price - promo_cost
                    context['promo_cost'] = promo_cost
                    context['promo_success'] = 'ใช้โค้ด '+promotion_info.name+ ' สำเร็จ'   
            else:
                context['promo_error'] = 'ใช้โค้ดไม่สำเร็จ ไม่มีโค้ดนี้อยู่'
        # hit button submit
        if is_submit == 'submited':
            user = request.user
            start_date = a
            end_date = b
            # Pending
            status = 'Pending'
            print(user.id)
            buy_order = Buy(
                status = status, 
                start_date = start_date, 
                end_date = end_date, 
                total_price = price, 
                customer_id = user, 
                product_id = product, 
            )
            if promotion_info:
                buy_order.promotion = promotion_info
            buy_order.save()
            return redirect('confirm',id_buy = buy_order.id)
    
    context['price'] = price
    context['amount_day'] = day
    context['product'] = product

    return render(request, 'Order/detail.html', context=context)

def detail(request, id_product):
    context = {}
    product = Product.objects.get(pk=id_product)
    context['product'] = product
    return render(request, 'Order/detail.html', context=context)

@login_required
def confirm(request, id_buy):
    context={}
    buy_order = Buy.objects.get(pk=id_buy)
    context['Buy'] = buy_order
    return render(request, 'Order/confirm.html', context=context)

@login_required
def reservation_list(request):
    context = {}
    user_id = request.user.id
    Buys = Buy.objects.filter(customer_id__id__contains=user_id).order_by("-id")
    context['Buys'] = Buys
    return render(request, 'Order/status.html', context=context)

def index(request):

    context = {}
    products = {}
    
    if request.method == 'POST':
        select = request.POST.get('selection')
        keyword = request.POST.get('keyword')
        context['keyword'] = keyword
        context['selection'] = select
        if request.user.is_superuser == True or request.user.is_staff == True:
            if select == 'year':
                products = Product.objects.filter(years=keyword)
            elif select == 'data':
                products = Product.objects.filter(data__icontains=keyword)
            elif select == 'name':
                products = Product.objects.filter(name__icontains=keyword)
            else:
                products = Product.objects.filter(  Q(years__contains=keyword) |
                                            Q(data__contains=keyword) |
                                            Q(name__icontains=keyword))
        else:
            if select == 'year':
                products = Product.objects.filter(years=keyword).exclude(status='HIDE')
            elif select == 'data':
                products = Product.objects.filter(data__icontains=keyword).exclude(status='HIDE')
            elif select == 'name':
                products = Product.objects.filter(name__icontains=keyword).exclude(status='HIDE')
            else:
                products = Product.objects.filter(  Q(years__contains=keyword) |
                                            Q(data__contains=keyword) |
                                            Q(name__icontains=keyword))
    else:
        if request.user.is_superuser == True or request.user.is_staff == True:
            products = Product.objects.all()
        else:
            products = Product.objects.all().exclude(status='HIDE')
    context['products'] = products

    return render(request,'Order/index.html',context=context)

@login_required
def add_edit_product(request):
    return redirect('index')

@login_required
def change_product(request):
    return redirect('index')

@login_required
def product_detail(request, id_product):
    context = {}
    product = Product.objects.get(pk=id_product)
    context['product'] = product
    return render(request, 'Order/product_detail.html',context=context)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def add_pro(request):
    form = add_product()
    return render(request, 'Order/add_pro.html', {'form':form})