from django.http.response import HttpResponse
from django.shortcuts import render


def page1(request):
    return render(request, 'page1.html', {'name':'Page 1'})