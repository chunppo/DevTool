# -*- coding: utf-8 -*-

from django.shortcuts import render
from functools import wraps

def decorator_function(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):  #1
        print '{} 함수가 호출되기전 입니다.'.format(original_function.__name__)
        return original_function(*args, **kwargs)  #2
    return wrapper_function

def decorator_function1(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):  #1
        print '{} 11111함수가 호출되기전 입니다.'.format(original_function.__name__)
        return original_function(*args, **kwargs)  #2
    return wrapper_function

@decorator_function
@decorator_function1
def index(request):
    context = {
        'name': 'chunppo'
    }
    return render(request, 'index.html', context);