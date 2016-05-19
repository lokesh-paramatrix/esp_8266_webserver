from django.http.response import HttpResponse
from django.views.generic import View

class LedStatus(View):
    def get(self, request):
        print("*********",request.GET, request)
        print("Value = ", request.GET.get('led'))
        print("*********")
        return HttpResponse('<H1>Success</H1>')
