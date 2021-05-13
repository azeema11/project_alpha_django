from django.http.response import HttpResponse


def app1(request):
    return HttpResponse("App 1")