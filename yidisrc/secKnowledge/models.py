from django.db import models

# Create your models here.

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

class SecKnowledge(models.Model):
    id = models.AutoField(primary_key=True)
    vultitle = models.CharField(max_length=128)
    vulgroup = models.CharField(max_length=128)
    vuldesc = models.TextField()
    vulcause = models.TextField()
    attackmethod = models.TextField()
    vulsolution = models.TextField()
    referdoc = models.TextField()
    pubTime = models.DateTimeField(auto_now=True)

