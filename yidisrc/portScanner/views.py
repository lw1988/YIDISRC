from django.shortcuts import render
import nmap # 导入nmap库

from .models import *

# Create your views here.

def portscanner(request):

    if request.method == "GET":

        return render(request, "portScanner/portScanner.html")  # 此处跳转到前端页面时需要使用双引号

    elif request.method == "POST":

        # 获取前端传递的ip与port
        ip = request.POST.get("ip")
        port = request.POST.get("port")

        # 通过使用nmap.PortScanner()生成nmap对象，借用对象的scna方法执行nmap端口扫描
        nm = nmap.PortScanner()
        ret = nm.scan(str(ip),str(port))

        for host in nm.all_hosts():
            print('nm[host]---->',nm[host])
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())

        # PortScanner.objects.create(ip_addres = )

        # 模板到前端渲染
        return render(request, "portScanner/portScanner.html",
                      {"all_scan_result": ret})