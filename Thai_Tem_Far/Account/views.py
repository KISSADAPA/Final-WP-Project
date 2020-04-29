from builtins import object

from astroid.scoped_nodes import objects
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render

from Account.models import Customer, Staff


# Create your views here.
def register_page(request):

    context = {}

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if con_pass != password:
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['email'] = email
            context['phone'] = phone
            context['address'] = address
            context['username'] = username
            context['error'] = 'Password do not match'
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
                user.save()

                customer = Customer (
                    cus_fname = first_name,
                    cus_lname = last_name,
                    cus_email = email,
                    cus_phone = phone,
                    cus_address = address,
                    account = User.objects.get(username=username)
                )
                customer.save()
                return redirect('login')

            except Exception as e:
                context['first_name'] = first_name
                context['last_name'] = last_name
                context['email'] = email
                context['phone'] = phone
                context['address'] = address
                context['error'] = 'Someone already has this Username. Try another name.'

    return render(request, 'Account/register.html', context=context)

def register_staff_page(request):

    context = {}

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if con_pass != password:
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['email'] = email
            context['phone'] = phone
            context['position'] = position
            context['username'] = username
            context['error'] = 'Password do not match'
        else:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_staff = True
                group = Group.objects.get(name='Staff')
                user.groups.add(group)
                user.save()

                staff = Staff (
                    sta_fname = first_name,
                    sta_lname = last_name,
                    sta_email = email,
                    sta_phone = phone,
                    sta_position = position,
                    account = User.objects.get(username=username)
                )
                staff.save()
                return redirect('login')

    return render(request, 'Account/register_staff.html', context=context)

def login_page(request):
    
    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['error'] = 'Username or Password is not Correct'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, 'Account/login.html', context=context)

@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

def change_pass(request):

    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if con_pass != password:
            context['username'] = username
            context['error'] = 'Password do not match'
        else:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return redirect('login')

    return render(request, 'Account/change_pass.html', context=context)

@login_required
def profile_page(request):

    user = request.user
    customer = Customer.objects.get(account = user)

    context = {
        'user': user,
        'customer': customer
    }

    return render(request, 'Account/profile.html', context=context)


@login_required
def profile_staff_page(request):

    user = request.user
    staff = Staff.objects.get(account = user)

    context = {
        'user': user,
        'staff': staff
    }

    return render(request, 'Account/profile_staff.html', context=context)

@login_required
def edit_profile_page(request):

    context = {}

    user = request.user
    customer = Customer.objects.get(account = user)

    first_name = customer.cus_fname
    last_name = customer.cus_lname
    email = customer.cus_email
    phone = customer.cus_phone
    address = customer.cus_address
    username = user.username

    context['first_name'] = first_name
    context['last_name'] = last_name
    context['email'] = email
    context['phone'] = phone
    context['address'] = address
    context['username'] = username

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if con_pass != password:
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['email'] = email
            context['phone'] = phone
            context['address'] = address
            context['username'] = username
            context['error'] = 'Password do not match'
        else:
            customer.cus_fname = first_name
            customer.cus_lname = last_name
            customer.cus_phone = phone
            customer.cus_address = address
            customer.save()

            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.save()

            return redirect('profile')

    return render(request, 'Account/edit_profile.html', context=context)

@login_required
def edit_profile_staff_page(request):

    context = {}

    user = request.user
    staff = Staff.objects.get(account = user)

    first_name = staff.sta_fname
    last_name = staff.sta_lname
    email = staff.sta_email
    phone = staff.sta_phone
    position = staff.sta_position
    username = user.username

    context['first_name'] = first_name
    context['last_name'] = last_name
    context['email'] = email
    context['phone'] = phone
    context['position'] = position
    context['username'] = username

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if con_pass != password:
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['email'] = email
            context['phone'] = phone
            context['position'] = position
            context['username'] = username
            context['error'] = 'Password do not match'
        else:
            staff.sta_fname = first_name
            staff.sta_lname = last_name
            staff.sta_phone = phone
            staff.sta_position = position
            staff.save()

            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.save()

            return redirect('profile_staff')

    return render(request, 'Account/edit_profile_staff.html', context=context)