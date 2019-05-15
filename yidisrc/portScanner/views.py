from django.shortcuts import render
import nmap # 导入nmap库
import datetime,time,os

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

def nmap_A_scan(network_prefix,scan_port,port_white_list):
    nm = nmap.PortScanner()

    # 执行nmap端口扫描
    scan_result = nm.scan(hosts=network_prefix,arguments='-p' + scan_port)


    # 分析扫描结果
    for host,result in scan_result['scan'].items():
        if result['status']['state'] == 'up':
            try:
                for port in result['tcp']:
                    if port in port_white_list:
                        print(host,'<----->',port)
                        # 将高风险端口写入数据库
                        AutoPortScanner.objects.create(ip_address=host, port_num=str(port),
                                                   port_status=result['tcp'][port]['state'])
            except:
                pass

def autoportscanner(request):

    if request.method == "GET":

        data_from_db = AutoPortScanner.objects.all()
        today = time.strftime('%Y-%m-%d', time.localtime())

        # 此处跳转到前端页面时需要使用双引号
        return render(request, "portScanner/autoPortScanner.html",
                      {"all_scan_result": data_from_db,"today":today})
    #
    # elif request.method == "POST":
    #     # 生成当日日期，格式例如2019-01-01
    #     start_time = time.strftime('%Y-%m-%d',time.localtime())
    #
    #     network_prefix = request.POST.get("ip")
    #     scan_port = request.POST.get("port")
    #
    #     port_white_list = [22,3389,3306,5432,27017,9200,9300,6379,2181,9092,50070,8088,60010,10000]
    #
    #     nmap_A_scan(network_prefix, scan_port, port_white_list)
    #
    #     return render(request, "portScanner/autoPortScanner.html",
    #                   {"all_scan_result": "Hello world!!!"})

def editautoportscanner(request):

    if request.method == "GET":
        return render(request, "portScanner/editAutoPortScanner.html")

    elif request.method == "POST":

        # 生成当日日期，格式例如2019-01-01
        start_time = time.strftime('%Y-%m-%d', time.localtime())

        network_prefix = request.POST.get("ip")
        scan_port = request.POST.get("port")
        vul_portarea = request.POST.get("vul_portarea")
        vul_portarea = '['+vul_portarea+']'

        port_white_list = [22, 3389, 3306, 5432, 27017, 9200, 9300, 6379, 2181, 9092, 50070, 8088, 60010, 10000]
        port_white_list = eval(vul_portarea)

        # 用户在前端输入多个ip，ip之间需要用逗号分割开
        ip_list = network_prefix.split(',')

        for target_ip in ip_list:
            nmap_A_scan(target_ip, scan_port, port_white_list)

        data_from_db = AutoPortScanner.objects.all()
        today = time.strftime('%Y-%m-%d', time.localtime())

        # 此处跳转到前端页面时需要使用双引号
        return render(request, "portScanner/autoPortScanner.html",
                      {"all_scan_result": data_from_db,"today":today})