from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Status
from .misc import *

def home(request):
    latest_query = Status.objects.all().order_by('-timestamp')[0]

    latest_reports = get_hosts_and_ports()
    status_context = {'port_status': latest_reports,
                      'latest_query': latest_query.timestamp}

    return render(request, 'home.html', context=status_context)

def table(request):
    # get all parameter
    ip = request.GET.get('ip', '')
    port = request.GET.get('port', '')
    n_page = request.GET.get('page', 1)
    daterange = request.GET.get('daterange', '')

    prev_url = request.META.get('HTTP_REFERER')
    path = remove_page(request.get_full_path())

    # each pagination display 100 rows of data
    data_row = 100

    status_context = { 'ip': ip,
            'port': port,
            'current_path': path,
            'prev_url': prev_url}

    if daterange != '':
        '''
        this block is executed
        if daterange parameter is specified
        '''
        startDate, stopDate = daterange.split(" - ")
        start_date = string_to_time(startDate)
        stop_date = string_to_time(stopDate, "stop")

        # get the latest status data
        status_data = Status.objects.filter(
            host=ip, port=port, timestamp__gte=start_date,
            timestamp__lte=stop_date).order_by('-timestamp')

    else:
        # get the latest status data
        status_data = Status.objects.filter(
            host=ip, port=port).order_by('-timestamp')

    pginator = Paginator(status_data, data_row)
    page_range = paginate(int(n_page), list(pginator.page_range))

    # display data row as much as n_page
    status_data = pginator.page(n_page)

    status_context['page_range'] = page_range
    status_context['port_status'] = status_data

    # render pagination
    return render(request, 'table.html', context=status_context)
