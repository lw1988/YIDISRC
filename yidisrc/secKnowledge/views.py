from django.shortcuts import render
from .models import *
# Create your views here.

def commonSecKnowledge(request):
    return render(request,"secKnowledge/secKnowledge.html")

def webSecKnowledge(request):
    return render(request, "secKnowledge/secKnowledge.html")

def appSecKnowledge(request):
    return render(request, "secKnowledge/secKnowledge.html")

def editSecKnowledge(request):

    if request.method == "GET":
        return render(request, "secKnowledge/editSecKnowledge.html")

    elif request.method == "POST":

        """
        漏洞标题：VulTitle   =》 漏洞名称
        漏洞分组：VulGroup   =》 漏洞是属于通用软件类，还是web或是app类
        漏洞描述：VulDesc
        漏洞成因：VulCause
        攻击方法：AttackMethod
        解决方案：VulSolution
        参考文档：ReferDoc
        发布时间：pubTime
        """
        # 从前端Form中读取漏洞信息
        vultitle = request.POST.get("vultitle")
        vulgroup = request.POST.get("vulgroup")
        vuldesc = request.POST.get("vuldesc")
        vulcause = request.POST.get("vulcause")
        attackmethod = request.POST.get("attackmethod")
        vulsolution = request.POST.get("vulsolution")
        referdoc = request.POST.get("referdoc")

        # 将创建的漏洞信息写入数据库
        SecKnowledge.objects.create(vultitle=vultitle,
                                    vulgroup=vulgroup,
                                    vuldesc=vuldesc,
                                    vulcause=vulcause,
                                    attackmethod=attackmethod,
                                    vulsolution=vulsolution,
                                    referdoc=referdoc
                                    )

        # 从数据库中读取数据，然后渲染到前端模板

        vul_data_from_db = SecKnowledge.objects.all()

        return render(request, "secKnowledge/secKnowledge.html",{"data":vul_data_from_db})