# wxproject

微信扫码授权

用到的包
json
requests

1.填写参数到接口里，制作二维码。

参数：
  appid
  redirect_uri
  response_type
  scope
  state
  
2.调取上述接口，得到 code 参数。

3.请求接口，通过得到的 code 参数，获取 access_token参数。

参数：
  appid
  secret
  code
  grant_type

4.请求用户信息接口，获取用户信息。

参数：
  access_token
  openid
  lang
  
5.通过 django 项目，把拿到的用户信息展示到前端页面。
