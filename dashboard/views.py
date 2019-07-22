from django.shortcuts import render
from .dict_builder import retrieve

# Create your views here.
status_data = retrieve()


def home(request):
    ips = {'ips': status_data.keys}
    return render(request, 'home.html', context=ips)

def table(request):
    ip = request.GET.get('ip', '')
    var = {'ip': ip }

    # if the ip is not exist in dictionary
    try:
        var.update({'port_status': status_data[ip]})
    except KeyError:
        var.update({'port_status': False})

    return render(request, 'table.html', context=var)
