from django.http.response import HttpResponse


def app2(request):
    return HttpResponse("Hello App 2")