# _*_ encoding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime, time

# Create your models here.

class Asset(models.Model):
    ip_pub = models.GenericIPAddressField(max_length=50, verbose_name=u'外网IP地址')
    #ip_prv = models.GenericIPAddressField(max_length=50, verbose_name=u'内网IP地址')
    hostname = models.CharField(max_length=50, verbose_name=u'主机名')
    os = models.CharField(max_length=50, verbose_name=u'操作系统')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU型号')
    cpu = models.CharField(max_length=50, verbose_name=u'CPU')
    mem = models.CharField(max_length=50, verbose_name=u'内存')
    disk = models.CharField(max_length=50, verbose_name=u'硬盘')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
 
    class Meta:
        verbose_name = u"资产信息表"
	verbose_name_plural = verbose_name
	ordering = ['ip_pub']
    
    def __unicode__(self):
        return self.ip_pub

class Host(models.Model):
    ip_pub = models.GenericIPAddressField(max_length=20, verbose_name=u'外网IP地址')
    ip_prv = models.GenericIPAddressField(max_length=20, null=True, blank=True, verbose_name=u'内网IP地址')
    username = models.CharField(max_length=20, verbose_name=u'用户名')
    pwd_root = models.CharField(max_length=100, verbose_name=u'root登录密码')
    pwd_user = models.CharField(max_length=100, verbose_name=u'普通用户登录密码')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'上次检测时间')
    status = models.CharField(max_length=50, verbose_name=u'添加状态')
    
    class Meta:
        verbose_name = u"主机信息表"
        verbose_name_plural = verbose_name
        ordering = ['ip_pub']

    def __unicode__(self):
        return self.ip_pub
