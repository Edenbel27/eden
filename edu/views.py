from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def post_list(request):

    return HttpResponse("Hello world, you are at the polls index")
