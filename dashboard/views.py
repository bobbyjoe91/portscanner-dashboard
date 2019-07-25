from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Status
from .date_parser import string_to_time

# Create your views here.

def home(request):
    status_data = Status.objects.all()
    status_context = {'port_status': status_data}
    return render(request, 'home.html', context=status_context)

def table(request):
    # get all parameter
    ip = request.GET.get('ip', '')
    port = request.GET.get('port', '')
    n_page = request.GET.get('page', 1)
    daterange = request.GET.get('daterange', '')

    path = request.get_full_path()

    # each pagination display 50 rows of data
    data_row = 50

    status_context = { 'ip': ip,
            'port': port,
            'daterange': path}

    if daterange != '':
        '''
        this block is executed
        if daterange parameter is specified
        '''
        startDate, stopDate = daterange.split(" - ")
        start_date = string_to_time(startDate)
        stop_date = string_to_time(stopDate, "")

        # get the latest status data
        status_data = Status.objects.filter(
            host=ip, port=port, timestamp__gte=start_date,
            timestamp__lte=stop_date).order_by('-timestamp')

    else:
        # get the latest status data
        status_data = Status.objects.filter(
            host=ip, port=port).order_by('-timestamp')

    pginator = Paginator(status_data, data_row)

    # display data row as much as n_page
    status_data = pginator.page(n_page)

    status_context['port_status'] = status_data

    # render pagination
    return render(request, 'table.html', context=status_context)
