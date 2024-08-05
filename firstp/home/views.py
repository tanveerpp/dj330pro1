from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp
from django.db.models import Max,Min,Avg,Sum
async def index(request):
    #return HttpResponse("My Project is running")
    #return HttpResponse("<h1>My Project is running</h1>")
    mx=await Emp.objects.all().aaggregate(Max('sal'))
    mn=await Emp.objects.all().aaggregate(Min('sal'))
    ag=await Emp.objects.all().aaggregate(Avg('sal'))
    sm=await Emp.objects.all().aaggregate(Sum('sal'))
    return render(request,'index.html',{'mx':mx,'mn':mn,'ag':ag,'sm':sm})
