from django.shortcuts import render
# from django import forms
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def view(request):
    if request.method=='GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        map = request.POST.get('map',default=None)
        return render(request, 'index.html',{'map':map})
