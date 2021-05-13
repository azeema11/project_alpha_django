from django.http.response import HttpResponse
from django.shortcuts import render


def app3(request):
    return render(request, 'hello.html', {'name':'Martin'})