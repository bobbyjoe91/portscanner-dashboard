from django.shortcuts import render
from .models import Status

# Create your views here.

def home(request):
    widget_data = Status.objects.all()
    var = {'port_status': widget_data}
    return render(request, 'home.html', context=var)

def table(request):
    ip = request.GET.get('ip', '')
    port = request.GET.get('port', '')
    daterange = request.GET.get('daterange', '')

    print(daterange)
    var = { 'ip': ip,
            'port': port}

    if daterange != '':
        var['port_status'] = retrieve_by_ip_port_and_daterange(ip, port, daterange)
    else:
        var['port_status'] = Status.objects.filter(host=ip, port=port)
        # retrieve_by_ip_and_port(ip, port)

    return render(request, 'table.html', context=var)
