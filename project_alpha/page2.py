from django.http.response import HttpResponse
from django.shortcuts import render


def page2(request):
    return render(request, 'page2.html', {'name':'Page 2'})