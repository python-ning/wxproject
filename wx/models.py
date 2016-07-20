# coding:utf-8
from django.db import models


class WechatUserInfo(models.Model):
    openid = models.CharField(max_length=30, verbose_name='openid')
    nickname = models.CharField(max_length=30, verbose_name='微信名')
    sex = models.CharField(max_length=30, verbose_name='性别')
    language = models.CharField(max_length=30, verbose_name='语言')
    city = models.CharField(max_length=30, verbose_name='城市')
    province = models.CharField(max_length=30, verbose_name='省份')
    country = models.CharField(max_length=30, verbose_name='国家')
    headimgurl = models.CharField(max_length=30, verbose_name='头像')
    privilege = models.CharField(max_length=30, verbose_name='特权')
