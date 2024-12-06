import re
import json
from curl_cffi import requests#因为tls指纹，所以用的别人写好的
import chardet
from bs4 import BeautifulSoup
import  pymysql
import urllib3
import io
def net_connected():
    s = socket.socket()
    s.settimeout(1)
    try:
        status = s.connect_ex(('www.baidu.com', 443))
        if status == 0:
            s.close()
            return True
        else:
            s.close()
            return False
    except Exception as e:
        return False
with open('account.txt','r') as file:
    content = file.read()
    content = eval(content)
    print(type(content))
admin = content['admin']
passwd = content['passwd']
url1 = 'http://edge-http.microsoft.com/captiveportal/generate_204'#每个人的认证url是不一样的，没有通用的
r = requests.get(url=url1,verify=False)
print(r.url)
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "441",
    "content-type": "application/x-www-form-urlencoded",
    "host": "portal.sicau.edu.cn",
    "origin": "https://portal.sicau.edu.cn",
    "pragma": "no-cache",
    "referer": r.url,
    "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

data = {
    "scheme": "https",
    "serverIp": "portal.sicau.edu.cn:443",
    "hostIp": "http://127.0.0.1:8443/login",
    "Type": "auth",
    "auth_type": "0",
    "isBindMac1": "0",
    "pageid": "201",
    "templatetype": "1",
    "listbindmac": "0",
    "recordmac": "0",
    "isRemind": "1",
    "loginTimes": "",
    "groupId": "",
    "distoken": "",
    "echostr": "",
    "url": "",
    "isautoauth": "",
    "mobile": "",
    "notice_pic_loop1": "/portal/uploads/pc/demo3/images/logo.jpg",
    "notice_pic_loop2": "/portal/uploads/pc/demo3/images/rrs_bg.jpg",
    "userId": admin,
    "passwd": passwd,
    "remInfo": "on"
}
r2 = requests.post(url=r.url,data=data,headers=headers)
if(r.status_code==200 and net_connected):
    print('服务器已接受表单,并且网络已连接,若网络没有连接请再次运行一次程序.')
else:
    print('失败,可能是因为已经完成了认证.')