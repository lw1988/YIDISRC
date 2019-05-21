from django.shortcuts import render

# Create your views here.

def vmslist(request):
    if request.method == "GET":
        vul_content = "hello"
        return render(request, "vms/vmslist.html",{"vul_content": vul_content})

def vmsadd(request):
    if request.method == "GET":
        return render(request,"vms/vmsadd.html")