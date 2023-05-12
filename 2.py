import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 



 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="noahwsl@163.com"    #用户名
mail_pass="NJAYPANJKMGUXVHS"   #口令 
 
 
sender = 'noahwsl@163.com'
receivers = ['noahwsl@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('网络不稳定', 'plain', 'utf-8')
message['From'] = Header("网络状态", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = '网络状态监测'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    while True:
        ret = os.system("ping baidu.com -n 4")
        if ret == False:
            print(ret)
            time.sleep(60)
        else:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
            time.sleep(60)
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")