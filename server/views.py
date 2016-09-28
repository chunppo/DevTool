# -*- coding: utf-8 -*-

from DevTool.serializer import ResultSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import ServerGroup
from .models import ServiceServer

import json

"""
서버그룹 리스트 뷰
"""
def server_group(request):
    group_list = ServerGroup.objects.all()
    context = {'group_list': group_list}
    return render(request, 'server/group.html', context);

def server_group_add(request):
    query_set = ServerGroup.objects.all()
    result = ResultSerializer().serialize(query_set)
    context = {"data": json.loads(result)}
    return JsonResponse(context)

def list(request):
    context = {
        'name': 'chunppo'
    }

    p = ServerGroup.objects.exclude(
        sever_group_id=ServiceServer.objects.filter(
            host_name='1111',
        ),
    ).select_related('description').values()

    a = ServiceServer.objects.all().prefetch_related('sever_group_id')
    # for a in p:
    #    print a
    # print p.group_name
    return render(request, 'server/list.html', context);
