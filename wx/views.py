# encoding=utf-8
from django.shortcuts import render,HttpResponse
from models import WechatUserInfo
import requests
import json
from django.core.cache import cache

APPID = "wx2e4b3f5d864ec373"
SECRET = "34420c2496cbb60d75e02e1ef1bb8183"
SEX = {1:u'男', 2:u'女'}


def index(request):
    code = request.GET['code']
    if cache.get(code) is None:
        access_token_data = {
            "appid": APPID,
            "secret": SECRET,
            "code": code,
            "grant_type": "authorization_code"
        }
        url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        params = json.loads(requests.get(url, params=access_token_data).content)
        url = "https://api.weixin.qq.com/sns/userinfo"
        data = {
            "access_token": params['access_token'],
            "openid": params['openid'],
            "lang": "zh_CN"
        }
        paramss = json.loads(requests.get(url, params=data).content)
        data = {
            'openid': paramss['openid'],
            'nickname': paramss['nickname'],
            'sex': SEX[paramss['sex']],
            'language': paramss['language'],
            'city': paramss['city'],
            'province': paramss['province'],
            'country': paramss['country'],
            'headimgurl': paramss['headimgurl']
        }
        cache.set(code, data, 60)
    else:
        data = cache.get(code)
    return render(request, 'index.html', data)
