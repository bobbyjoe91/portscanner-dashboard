from django.shortcuts import render
from .dict_builder import *

# Create your views here.
# detailed_status_data = retrieve('All')
widget_data = retrieve_latest_ip_and_port()

def home(request):
    var = {'port_status': widget_data}
    return render(request, 'home.html', context=var)

def table(request):
    ip = request.GET.get('ip', '')
    port = request.GET.get('port', '')
    daterange = request.GET.get('daterange', '')

    if daterange != '':
        var = {'port_status': retrieve_by_ip_port_and_daterange(ip, port, daterange),
                'ip': ip,
                'port': port}
    else:
        var = {'port_status': retrieve_by_ip_and_port(ip, port),
                'ip': ip,
                'port': port}

    return render(request, 'table.html', context=var)
