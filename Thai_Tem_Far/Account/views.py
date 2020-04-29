from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.shortcuts import redirect, render

from Account.models import Customer

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
            context['password'] = password
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
    return render(request, 'Account/profile.html')