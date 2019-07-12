from django.shortcuts import render
from dashboard.models import Status

# Create your views here.
def dummy(request):
    port_status = Status.objects.order_by('ip')
    var = {'port_status': port_status}
    return render(request, 'dummy.html', context=var)
