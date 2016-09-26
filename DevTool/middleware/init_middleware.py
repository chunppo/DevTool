class InitServerMiddleware(object):
    def __init__(self):
        #...
        print 'Custom __init__'
        pass

    def process_request(self, request):
        #...
        print 'Custom process_request'
        pass

    def process_exception(self, request, exception):
        #...
        print 'Custom process_exception'
        pass

    def process_response(self, request, response):
        #...
        print 'Custom process_response'
        return response

    def process_template_response(self, request, response):
        #...
        print 'Custom process_template_response'
        return response