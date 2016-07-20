# encoding=utf-8
from django.shortcuts import render
from models import WechatUserInfo
import requests
import json
from django.core.cache import cache

APPID = "wx2e4b3f5d864ec373"
SECRET = "34420c2496cbb60d75e02e1ef1bb8183"
SEX = {1:u'男', 2:u'女'}


def index(request):
    # print request.GET
    code = request.GET['code']
    access_token_data = {
        "appid": APPID,
        "secret": SECRET,
        "code": code,
        "grant_type": "authorization_code"
    }
    url = "https://api.weixin.qq.com/sns/oauth2/access_token"
    params = json.loads(requests.get(url, params=access_token_data).content)
    # print params
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
    cache.set("openid", paramss['openid'], 2 * 3600)
    cache.set("nickname", paramss['nickname'], 2 * 3600)
    cache.set("sex", SEX[paramss['sex']], 2 * 3600)
    cache.set("language", paramss['language'], 2 * 3600)
    cache.set("city", paramss['city'], 2 * 3600)
    cache.set("province", paramss['province'], 2 * 3600)
    cache.set("country", paramss['country'], 2 * 3600)
    cache.set("headimgurl", paramss['headimgurl'], 2 * 3600)

    openid = cache.get("openid", None)
    nickname = cache.get("nickname", None)
    sex = cache.get("sex", None)
    language = cache.get("language", None)
    city = cache.get("city", None)
    province = cache.get("province", None)
    country = cache.get("country", None)
    headimgurl = cache.get("headimgurl", None)

    data = {
        'openid': openid,
        'nickname': nickname,
        'sex': sex,
        'language': language,
        'city': city,
        'province': province,
        'country': country,
        'headimgurl': headimgurl
    }
    return render(request, 'index.html', data)
