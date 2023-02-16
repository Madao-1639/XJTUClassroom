from RequestClass import RequestClass,CookieError
from GetCookie import GetCookie
import os

username='XXX'                                  #学工号/手机号/NetID/身份证(Staff/Student ID/Mob)
password='XXX'                                  #请输入密码(Please enter the password)
retry=3                                         #重试次数
#buildings=['主楼A', '主楼B', '主楼C', '主楼D']  查询教学楼
#date='2020-01-01'                              查询日期(YYYY-MM-DD)                                        

for i in range(retry):
    if os.path.exists('Cookies'):
        with open('Cookies','r') as f:
            Cookies=f.read()
        try:
            RequestClass(Cookies)               #自定义教学楼和日期: RequestClass(Cookies,Buildings=['主楼A', '主楼B', '主楼C', '主楼D'],dateStr=date)
            break
        except CookieError:
            GetCookie(username,password)
    else:
        GetCookie(username,password)