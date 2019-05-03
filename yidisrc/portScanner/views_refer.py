from django.shortcuts import render
from . import models

# Create your views here.
import nmap
import time,os

# 参考：https://blog.csdn.net/Tong_T/article/details/80603378

'''
v3.1 在参考链接接触上优化，输出结果全部重定向到变量scan_result，且结果精简。
'''
scan_time = time.strftime('%Y-%m-%d',time.localtime())
log_dir = 'port_scanner/port_scan_log/'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_allPort = open(log_dir + scan_time + "_all_port_list.txt","w")
file_vulPort = open(log_dir + scan_time + "_vul_port_list.txt","w")

def port_scan(network_prefix,scan_port):
    nm = nmap.PortScanner()

    # 配置nmap扫描参数
    scan_raw_result = nm.scan(hosts=network_prefix, arguments='-p' + scan_port)
    # 分析扫描结果

    for host, result in scan_raw_result['scan'].items():


        # host_tag = 'Host: ' + host + '\n'
        # all_scan_result = all_scan_result + host_tag + '\n'

        try:
            if result['status']['state'] == 'up':
                all_scan_result = ""
                vul_scan_result = ""

            for port in result['tcp']:
                all_scan_result += '主机：'+host+ ' 端口号: ' + str(port) + '\t\t状态: ' + result['tcp'][port]['state']+'\n'

                models.PortScanner.objects.create(
                    ip_address = host,
                    port_num=port,
                    port_status = result['tcp'][port]['state']
                )

            file_allPort.write(all_scan_result)

            if port in [22,3389]:
                vul_scan_result += "主机："+host+" port:"+str(port)+ '\t\t状态: ' + result['tcp'][port]['state']+'\n'
                # file_vulPort.write("host:"+host+" port:"+str(port))

            return all_scan_result,vul_scan_result
        except:
            pass

def index(request):

    host_port_db = models.PortScanner.objects.all()
    # print('---->',type(host_port_db))

    if request.method == "GET":
        return render(request, "port_scanner/index.html", {"host_port_db": host_port_db})
        # for i in host_port_db:
        #     print('~~~>',type(i),i.ip_address,i.port_num,i.port_status)
        #
        #     # return render(request,"port_scanner/index.html",{"db_port_status":db_port_status})
        #     return render(request, "port_scanner/index.html",
        #                   {"ip_address":i.ip_address,
        #                    "port_num":i.port_num,
        #                    "port_status":i.port_status},
        #                   )

        # return render(request, "port_scanner/index.html",
        #               {"ip_address":1,
        #                "port_num":2,
        #                "port_status":3},
        #               )

    elif request.method == "POST":

        network_prefix = request.POST.get("ip")
        scan_port = request.POST.get("port")

        all_scan_result, vul_scan_result = port_scan(network_prefix,scan_port)
        return render(request, "port_scanner/index.html",{"all_scan_result":all_scan_result,"vul_scan_result":vul_scan_result})