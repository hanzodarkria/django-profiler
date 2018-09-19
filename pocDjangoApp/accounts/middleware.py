from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware(object):

    def __init__(self):
        pass
        # self.get_response = get_response
    #
    # def __call__(self, request):
    #     response = self.get_response(request)
    #     return response

