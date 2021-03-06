# encoding=utf-8
import json
import requests
from django.core.cache import cache
from django.shortcuts import render, HttpResponse


APPID = "wx2e4b3f5d864ec373"
SECRET = "34420c2496cbb60d75e02e1ef1bb8183"
SEX = {1: u'男', 2: u'女'}
LANGUAGE = {'zh_CN': u'汉语'}


def index(request):
    code = request.GET.get('code', None)
    if cache.get(code) is None:
        access_token_data = {
            "appid": APPID,
            "secret": SECRET,
            "code": code,
            "grant_type": "authorization_code"
        }

        # 拿到 code请求去拿 access_token
        url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        params = json.loads(requests.get(url, params=access_token_data).content)

        # 通过access_token和 openid 去拿用户信息
        url = "https://api.weixin.qq.com/sns/userinfo"
        data = {
            "access_token": params['access_token'],
            "openid": params['openid'],
            "lang": "zh_CN"
        }
        params = json.loads(requests.get(url, params=data).content)

        data = {
            'openid': params['openid'],
            'nickname': params['nickname'],
            'sex': SEX[params['sex']],
            'language': LANGUAGE[params['language']],
            'city': params['city'],
            'province': params['province'],
            'country': params['country'],
            'headimgurl': params['headimgurl']
        }
        cache.set(code, data, 60)
        return HttpResponse("OK")
    else:
        data = cache.get(code)
    return render(request, 'index.html', data)
