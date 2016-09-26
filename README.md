# DevTool

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

    a = ServiceServer.objects.filter(server_id=1).prefetch_related('sever_group_id')

    for zz in a:
        print zz.sever_group_id
    # for a in p:
    #    print a
    # print p.group_name
    return render(request, 'server/list.html', context);
