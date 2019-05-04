from django.shortcuts import render
import nmap # 导入nmap库

from .models import *

# Create your views here.

def portscanner(request):

    if request.method == "GET":

        data_from_db = PortScanner.objects.all()

        # 此处跳转到前端页面时需要使用双引号
        return render(request, "portScanner/portScanner.html",{"all_scan_result": data_from_db})

    elif request.method == "POST":

        # 获取前端传递的ip与port
        ip = request.POST.get("ip")
        port = request.POST.get("port")

        # 通过使用nmap.PortScanner()生成nmap对象，借用对象的scna方法执行nmap端口扫描
        nm = nmap.PortScanner()
        # ret = nm.scan(str(ip),str(port))
        scan_result = nm.scan(hosts=ip, arguments='-p' + port)

        # 每次手动扫描前将上一次手动扫描的结果在数据表中清空
        PortScanner.objects.all().delete()

        # 将最新扫描结果入库
        for host,result in scan_result['scan'].items():
            if result['status']['state'] == 'up':
                for scan_port in result['tcp']:
                    print('主机：%s\t端口：%s\t状态:%s\t' % (host,str(scan_port),result['tcp'][scan_port]['state']))
                    PortScanner.objects.create(ip_address = host,port_num = str(scan_port),port_status = result['tcp'][scan_port]['state'])

        # 取出最新扫描结果渲染到前端模板
        data_from_db = PortScanner.objects.all()
        return render(request, "portScanner/portScanner.html",
                      {"all_scan_result": data_from_db})

# 自动扫描

def autoportscanner(request):
    return render(request, "portScanner/autoPortScanner.html",
                  {"all_scan_result": "Hello world!!!"})