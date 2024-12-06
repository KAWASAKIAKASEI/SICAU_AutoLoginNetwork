import json
infor = open('account.txt','w+')
admin=input('输入你的网络认证账户:')
passwd=input('输入你的网络认证密码:')
data = {"admin": admin, "passwd": passwd}
data_str = json.dumps(data)
infor.write(data_str)