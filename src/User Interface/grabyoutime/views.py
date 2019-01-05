from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.urls import reverse

# Create your views here.
def home(request):
    context={}
    context['username']="Donna Snider"
    context['job']="Customer Support"
    context['place']="New York"
    context['year']=27
    context['time']="2011/01/25"
    context['money']="$112,000"
    return render(request,"dashboard.html",context)