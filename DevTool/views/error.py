from django.shortcuts import render_to_response
from django.template import RequestContext

def error_400(request):
    response = render_to_response('error/400.html', context_instance=RequestContext(request))
    response.status_code = 400
    return response

def error_404(request):
    response = render_to_response('error/404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response

def error_500(request):
    response = render_to_response('error/500.html', context_instance=RequestContext(request))
    response.status_code = 500
    return response