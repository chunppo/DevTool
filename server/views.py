from django.shortcuts import render
from .models import ServerGroup
from .models import ServiceServer

def index(request):
    context = {
        'name': 'chunppo'
    }

    p = ServerGroup.objects.exclude(
        sever_group_id=ServiceServer.objects.filter(
            host_name='1111',
        ),
    ).select_related('description').values()

    print p

    a = ServiceServer.objects.select_related('select_related').all()

    aa = a.sever_group_id

    print a
    print aa
    # for a in p:
    #    print a
    # print p.group_name
    return render(request, 'server/list.html', context);