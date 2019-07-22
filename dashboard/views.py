from django.shortcuts import render
from .dict_builder import retrieve

# Create your views here.
detailed_status_data = retrieve('All')
widget_data = retrieve(5)

def home(request):
    var = {'port_status': widget_data}
    return render(request, 'home.html', context=var)

def table(request):
    ip = request.GET.get('ip', '')
    port = request.GET.get('port', '')
    var = {'ip': ip }

    print(ip, port)
    # if the ip is not exist in dictionary
    try:
        var.update({'port_status': detailed_status_data[ip]})
    except KeyError:
        var.update({'port_status': False})

    return render(request, 'table.html', context=var)
