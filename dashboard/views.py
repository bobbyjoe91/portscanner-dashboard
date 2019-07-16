from django.shortcuts import render
from dashboard.models import Status

# Create your views here.

def home(request):
    port_status = Status.objects.order_by('ip')
    var = {'port_status': port_status}

    return render(request, 'home.html', context=var)
    # else:
    #     return render(request, 'pagination/head.html', context=var)
