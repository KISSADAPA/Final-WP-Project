from operator import index

from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return render(request, 'Order/index.html')
