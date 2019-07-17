from django.shortcuts import render
from dashboard.models import Status

# Create your views here.

def home(request):
    port_status = Status.objects.order_by('ip')
    var = {'port_status': port_status}

    return render(request, 'home.html', context=var)
    # else:
    #     return render(request, 'pagination/head.html', context=var)


def get_more_tables(request):
    increment = int(request.GET['append_increment'])
    increment_to = increment + 10
    port_status = Status.objects.filter(owner=request.user).order_by(
        'ip')[increment:increment_to]
    return render(request, 'get_more_tables.html', {'port_status': port_status})
