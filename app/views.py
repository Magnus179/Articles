from django.shortcuts import render
from .models import Articles
from django.db.models import Q
# Create your views here.
def index(req):
    data = Articles.objects.all()
    if req.method == 'POST':
        search = req.POST.get('search')
        data = Articles.objects.filter(title__contains=search)
        print(search)
    # print(data)
    context = {
        'data':data
    }
    return render(req,'index.html',context)
def details(req,pk):
    data1=Articles.objects.get(id=pk)
   
    context={
        'data1':data1
    }
    return render(req,'display.html',context)