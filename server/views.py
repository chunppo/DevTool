# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from DevTool.common.serializer import ResultSerializer

from .models import ServerGroup
from .models import ServiceServer

from django.core import serializers

"""
서버그룹 리스트 뷰
"""
def server_group(request):
    group_list = ServerGroup.objects.all()
    context = {'group_list': group_list}
    return render(request, 'server/group.html', context);

""""
서버그룹 호출
"""
def get_server_group(request):
    sever_group_id = request.GET['sever_group_id']

    try:
        query_set = ServerGroup.objects.get(
            sever_group_id=sever_group_id
        )
        print query_set
        result = ResultSerializer().serialize([query_set])
        json_result = json.loads(result[1:-1])
        context = {'result': 'success', "data": json_result}
        return JsonResponse(context)
    except ValidationError as e:
        context = {'result': 'fail'}
        return JsonResponse(context)

""""
서버그룹 저장
"""
@csrf_exempt
def server_group_add(request):
    server_group_name = request.POST['server_group_name']
    server_group_description = request.POST['server_group_description']

    try:
        model_server_group = ServerGroup(
            group_name=server_group_name,
            description=server_group_description,
            changer_account='chunppo')
        model_server_group.save()

        context = {'result': 'success'}
        return JsonResponse(context)
    except ValidationError as e:
        context = {'result': 'fail'}
        return JsonResponse(context)

""""
서버그룹 삭제
"""
@csrf_exempt
def server_group_remove(request):
    sever_group_id = request.POST['sever_group_id']

    try:
        ServerGroup.objects.get(
            sever_group_id=sever_group_id).delete()

        context = {'result': 'success'}
        return JsonResponse(context)
    except ValidationError as e:
        context = {'result': 'fail'}
        return JsonResponse(context)


    # query_set = ServerGroup.objects.all()
    # result = ResultSerializer().serialize(query_set)
    # json_result = json.loads(result)
    # context = {"data": json_result}
    # return JsonResponse(context)

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

