from django.shortcuts import render

# Create your views here.

def portscanner(request):

    if request.method == "GET":

        return render(request, "portScanner/portScanner.html")  # 此处跳转到前端页面时需要使用双引号

    elif request.method == "POST":

        ip = request.POST.get("ip")
        port = request.POST.get("port")

        all_scan_result = "当前IP："+ip+", 端口："+port

        print('all_scan_result',all_scan_result)

        return render(request, "portScanner/portScanner.html",
                      {"all_scan_result": all_scan_result})